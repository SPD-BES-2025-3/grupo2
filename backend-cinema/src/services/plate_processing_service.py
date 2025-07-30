import logging
from typing import Optional
from datetime import datetime

from models.dtos.plate_image_event import PlateImageEvent, PlateEventType
from services.ocr_service import OCRService
from services.plate_detection_service import PlateDetectionService
from repositories.reserva_repository import ReservaRepository
from models.reserva_model import StatusReservaEnum

logger = logging.getLogger(__name__)


class PlateProcessingService:
    """Serviço para processar eventos de placas e integrar com o sistema de reservas."""
    
    def __init__(self, reserva_repository: Optional[ReservaRepository] = None):
        self.ocr_service = OCRService()
        self.plate_detection_service = PlateDetectionService()
        self.reserva_repository = reserva_repository or ReservaRepository()
        
    async def process_image_event(self, event: PlateImageEvent) -> PlateImageEvent:
        """
        Processa um evento de imagem de placa seguindo o pipeline completo.
        
        PIPELINE:
        1. Detectar placa na imagem completa (PyTorch + OpenCV)
        2. Extrair região da placa (bounding box)
        3. Processar região com OCR (apenas se placa foi detectada)
        4. Verificar placa no sistema de clientes
        5. Validar reserva se cliente encontrado
        
        Args:
            event: Evento de imagem recebido
            
        Returns:
            Evento atualizado com resultado do processamento
        """
        try:
            logger.info(f"🚀 Iniciando pipeline de processamento: {event.id}")
            
            # ETAPA 1: Detectar placa na imagem completa
            event = await self._detect_plate_in_image(event)
            
            # Se não detectou placa, parar pipeline
            if event.event_type == PlateEventType.PLATE_NOT_DETECTED:
                logger.warning("❌ Pipeline interrompido - placa não detectada")
                return event
            
            # ETAPA 2: Processar região da placa com OCR
            event = await self._process_plate_with_ocr(event)
            
            # Se OCR falhou, parar pipeline  
            if not event.detected_plate:
                event.event_type = PlateEventType.PLATE_NOT_DETECTED
                event.error_message = "OCR não conseguiu ler a placa"
                logger.warning("❌ Pipeline interrompido - OCR falhou")
                return event
            
            # ETAPA 3: Verificar placa no sistema
            event = await self._check_plate_in_system(event)
            
            # ETAPA 4: Se placa encontrada, validar reserva
            if event.event_type == PlateEventType.PLATE_MATCHED:
                event = await self._validate_reservation(event)
            
            logger.info(f"✅ Pipeline concluído: {event.event_type}")
            return event
            
        except Exception as e:
            logger.error(f"❌ Erro no pipeline de processamento: {e}")
            event.event_type = PlateEventType.PLATE_NOT_DETECTED
            event.error_message = str(e)
            return event

    async def _detect_plate_in_image(self, event: PlateImageEvent) -> PlateImageEvent:
        """
        ETAPA 1: Detecta placa na imagem usando PyTorch e OpenCV.
        
        Args:
            event: Evento com imagem completa do veículo
            
        Returns:
            Evento atualizado com região da placa ou erro
        """
        try:

            if not event.image_base64:
                event.event_type = PlateEventType.PLATE_NOT_DETECTED
                return event
            
            logger.info("ETAPA 1: Detectando placa na imagem completa...")
            
            # Detectar e extrair região da placa usando PyTorch
            plate_region_base64 = await self.plate_detection_service.detect_plate_in_image(
                event.image_base64
            )
            
            if plate_region_base64:
                event.image_base64 = plate_region_base64
                event.event_type = PlateEventType.PLATE_DETECTED
            else:
                event.event_type = PlateEventType.PLATE_NOT_DETECTED
                event.error_message = "Nenhuma placa detectada na imagem"

            return event

                
        except Exception as e:
            logger.error(f"Erro na detecção de placa: {e}")
            event.event_type = PlateEventType.PLATE_NOT_DETECTED
            event.error_message = f"Erro na detecção: {str(e)}"
            
        return event

    async def _process_plate_with_ocr(self, event: PlateImageEvent) -> PlateImageEvent:
        """
        ETAPA 2: Processa região da placa extraída com OCR.
        
        Args:
            event: Evento com região da placa em image_base64
            
        Returns:
            Evento atualizado com texto da placa detectado
        """
        try:
            logger.info("ETAPA 2: Processando região da placa com OCR...")
            
            # Usar OCR apenas na região da placa (já extraída)
            result = await self.ocr_service.detect_plate(event.image_base64)
            
            if result and result.get('plate'):
                event.detected_plate = result['plate']
                event.confidence_score = result.get('confidence', 0.0)
                logger.info(f"✅ OCR detectou placa: {event.detected_plate} (confiança: {event.confidence_score})")
            else:
                event.confidence_score = 0.0
                logger.warning("❌ OCR não conseguiu ler a região da placa")
                
        except Exception as e:
            logger.error(f"Erro no OCR: {e}")
            event.confidence_score = 0.0
            
        return event

    async def _check_plate_in_system(self, event: PlateImageEvent) -> PlateImageEvent:
        """
        ETAPA 3: Verifica se a placa detectada existe no sistema através das reservas.
        
        Args:
            event: Evento com placa detectada pelo OCR
            
        Returns:
            Evento atualizado com informações da reserva
        """
        try:
            logger.info(f"ETAPA 3: Verificando placa {event.detected_plate} no sistema...")
            
            # Buscar reserva pela placa
            reserva = await self._find_reserva_by_plate(event.detected_plate)
            
            if reserva:
                event.cliente_id = str(reserva.cliente_id)
                event.reservation_id = str(reserva.id)
                event.session_id = str(reserva.sessao_id)
                event.reservation_status = reserva.status
                event.event_type = PlateEventType.PLATE_MATCHED
                logger.info(f"✅ Placa encontrada - Reserva: {reserva.id}")
            else:
                event.event_type = PlateEventType.PLATE_NOT_FOUND
                event.error_message = f"Placa {event.detected_plate} não possui reserva ativa no sistema"
                logger.warning(f"❌ Placa sem reserva ativa: {event.detected_plate}")
                
        except Exception as e:
            logger.error(f"Erro ao verificar placa no sistema: {e}")
            event.event_type = PlateEventType.PLATE_NOT_FOUND
            event.error_message = f"Erro ao verificar placa: {str(e)}"
            
        return event

    async def _validate_reservation(self, event: PlateImageEvent) -> PlateImageEvent:
        """
        ETAPA 4: Confirma a reserva se ela estiver pendente.
        
        Args:
            event: Evento com reserva identificada
            
        Returns:
            Evento atualizado com status da confirmação
        """
        try:
            logger.info(f"ETAPA 4: Confirmando reserva {event.reservation_id}...")
            
            if not event.reservation_id:
                return event
            
            # Se a reserva está pendente, confirmar
            if event.reservation_status == StatusReservaEnum.PENDENTE:
                reserva_atualizada = await self.reserva_repository.atualizar_status_reserva(
                    event.reservation_id, 
                    StatusReservaEnum.CONFIRMADA
                )
                
                if reserva_atualizada:
                    event.reservation_status = StatusReservaEnum.CONFIRMADA
                    logger.info(f"Reserva {event.reservation_id} confirmada com sucesso")
                else:
                    event.error_message = "Falha ao confirmar reserva"
                    logger.error(f"Falha ao confirmar reserva {event.reservation_id}")
                    
            elif event.reservation_status == StatusReservaEnum.CONFIRMADA:
                logger.info(f"Reserva {event.reservation_id} já estava confirmada")

            elif event.reservation_status == StatusReservaEnum.CANCELADA:
                event.error_message = "Reserva foi cancelada"
                logger.warning(f"Tentativa de confirmar reserva cancelada: {event.reservation_id}")

        except Exception as e:
            logger.error(f"Erro ao confirmar reserva: {e}")
            event.error_message = f"Erro ao confirmar reserva: {str(e)}"
            
        return event

    async def _find_reserva_by_plate(self, plate: str) -> Optional[object]:
        """
        Busca reserva pela placa usando o ReservaRepository.
        
        Args:
            plate: Placa a ser buscada
            
        Returns:
            Reserva encontrada ou None
        """
        try:
            # Buscar reservas pela placa
            reservas = await self.reserva_repository.listar_reservas_por_placa(plate)
            
            # Filtrar apenas reservas ativas (PENDENTE ou CONFIRMADA)
            reservas_ativas = [
                r for r in reservas 
                if r.status in [StatusReservaEnum.PENDENTE, StatusReservaEnum.CONFIRMADA]
            ]
            
            if reservas_ativas:
                # Retornar a primeira reserva ativa encontrada
                return reservas_ativas[0]
                
            return None
            
        except Exception as e:
            logger.error(f"Erro ao buscar reserva pela placa {plate}: {e}")
            return None

    async def create_plate_event_from_image(
        self, 
        gate_id: str, 
        image_base64: str, 
        image_path: Optional[str] = None
    ) -> PlateImageEvent:
        """
        Cria um evento de placa a partir de uma imagem.
        
        Args:
            gate_id: ID da catraca que capturou a imagem
            image_base64: Imagem em base64
            image_path: Caminho da imagem (opcional)
            
        Returns:
            Evento de placa criado
        """
        return PlateImageEvent(
            gate_id=gate_id,
            event_type=PlateEventType.PLATE_DETECTED,
            image_base64=image_base64,
            image_path=image_path,
            timestamp=datetime.now()
        )
