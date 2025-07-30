import asyncio
import json
from datetime import datetime

from models.dtos.plate_image_event import PlateImageEvent, PlateEventType
from infrastructure.adapters.mqtt_broker_adapter import MQTTBrokerAdapter, MQTTConfig
from config.config_manager import ConfigManager
from config.config_name import ConfigName
from services.plate_processing_service import PlateProcessingService

import logging

logger = logging.getLogger(__name__)


class PlateEventDrivenController:
    """Controller para processar eventos de placas via MQTT."""
    
    def __init__(self):
        # Configuração MQTT
        env_config = ConfigManager()
        mqtt_config = MQTTConfig(
    broker_host=env_config.get(ConfigName.MQTT_BROKER_HOSTNAME),
    broker_port=int(env_config.get(ConfigName.MQTT_BROKER_PORT)),
    client_id=f"{env_config.get(ConfigName.MQTT_BROKER_CLIENT_ID)}_plates"
    )

        logger.info(f"Conectando ao broker MQTT em {mqtt_config.broker_host}:{mqtt_config.broker_port}")

        # Inicializar adaptadores e serviços
        self.mqtt_broker = MQTTBrokerAdapter(mqtt_config)
        self.mqtt_broker.set_event_loop(asyncio.get_event_loop())
        self.plate_service = PlateProcessingService()
        
        # Registrar handlers para tópicos MQTT
        self._setup_mqtt_handlers()
        
        # Flag para controlar se está processando
        self.is_running = False
        
    def _setup_mqtt_handlers(self):
        """Configura o handler para o tópico MQTT."""
        # Handler único para eventos de imagem de placa
        self.mqtt_broker.register_handler(
            "cinema/plates/images", 
            self._handle_plate_image_event
        )
        
        logger.info("Handler MQTT configurado para cinema/plates/images")

    async def start(self):
        """Inicia o controller e conecta ao MQTT."""
        try:
            self.is_running = True
            self.mqtt_broker.connect()
            self.mqtt_broker.start()
            logger.info("PlateEventDrivenController iniciado com sucesso")
            
        except Exception as e:
            logger.error(f"Erro ao iniciar PlateEventDrivenController: {e}")
            raise

    async def stop(self):
        """Para o controller e desconecta do MQTT."""
        try:
            self.is_running = False
            self.mqtt_broker.stop()
            logger.info("PlateEventDrivenController parado")
            
        except Exception as e:
            logger.error(f"Erro ao parar PlateEventDrivenController: {e}")

    async def _handle_plate_image_event(self, topic: str, payload: str):
        """
        Processa mensagens simples de imagem recebidas via MQTT.
        
        Args:
            topic: Tópico MQTT da mensagem
            payload: JSON simples com gate_id, image_base64 e timestamp
        """
        try:
            logger.info(f"Mensagem recebida no tópico {topic}")
            
            data = json.loads(payload)
            
            event = PlateImageEvent(
                gate_id=data["gate_id"],
                event_type=PlateEventType.PLATE_DETECTED,  # Estado inicial
                image_base64=data["image_base64"],
                timestamp=datetime.fromisoformat(data["timestamp"].replace('Z', '+00:00'))
            )
            
            # Processar tudo: OCR + validação + reserva
            processed_event = await self.plate_service.process_image_event(event)
            
            await self._publish_result(processed_event)
            
            logger.info("Processamento concluído")
            
        except Exception as e:
            logger.error(f"Erro ao processar mensagem: {e}")
            await self._publish_error(str(e))

    async def _publish_result(self, event: PlateImageEvent):
        """
        Publica resultado do processamento no tópico de acesso.
        
        Args:
            event: Evento processado
        """
        try:
            # Determinar status de acesso baseado no resultado
            access_result = {
                "gate_id": event.gate_id,
                "plate": event.detected_plate,
                "timestamp": event.timestamp.isoformat(),
                "event_type": event.event_type,
                "access_granted": event.event_type == PlateEventType.PLATE_MATCHED and event.reservation_id is not None,
                "cliente_id": event.cliente_id,
                "reservation_id": event.reservation_id,
                "session_id": event.session_id,
                "confidence_score": event.confidence_score,
                "error_message": event.error_message
            }
            
            payload = json.dumps(access_result)
            self.mqtt_broker.publish("cinema/plates/access", payload)
            
            access_status = "AUTORIZADO" if access_result["access_granted"] else "NEGADO"
            logger.info(f"Resultado publicado: {access_status} para placa {event.detected_plate}")
            
        except Exception as e:
            logger.error(f"Erro ao publicar resultado: {e}")

    async def _publish_error(self, error_message: str):
        """
        Publica erro no tópico de acesso.
        
        Args:
            error_message: Mensagem de erro
        """
        try:
            error_result = {
                "gate_id": "unknown",
                "plate": None,
                "timestamp": datetime.now().isoformat(),
                "event_type": PlateEventType.PLATE_NOT_DETECTED,
                "access_granted": False,
                "error_message": error_message
            }
            
            payload = json.dumps(error_result)
            self.mqtt_broker.publish("cinema/plates/access", payload)
            
        except Exception as e:
            logger.error(f"Erro ao publicar erro: {e}")

    # Métodos para integração externa
    async def process_simple_image(self, gate_id: str, image_base64: str) -> dict:
        """
        Processa imagem simples e retorna resultado de acesso.
        
        Args:
            gate_id: ID da catraca
            image_base64: Imagem em base64
            
        Returns:
            Resultado de acesso formatado
        """
        # Criar evento inicial
        event = PlateImageEvent(
            gate_id=gate_id,
            event_type=PlateEventType.PLATE_DETECTED,
            image_base64=image_base64,
            timestamp=datetime.now()
        )
        
        # Processar tudo
        processed_event = await self.plate_service.process_image_event(event)
        
        # Retornar resultado formatado
        return {
            "gate_id": gate_id,
            "plate": processed_event.detected_plate,
            "access_granted": processed_event.event_type == PlateEventType.PLATE_MATCHED and processed_event.reservation_id is not None,
            "timestamp": processed_event.timestamp.isoformat(),
            "event_type": processed_event.event_type,
            "cliente_id": processed_event.cliente_id,
            "reservation_id": processed_event.reservation_id,
            "confidence_score": processed_event.confidence_score,
            "error_message": processed_event.error_message
        }