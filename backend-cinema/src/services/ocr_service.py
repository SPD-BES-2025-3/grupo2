import base64
import re
from typing import Dict, Optional
import logging
import cv2
import numpy as np
import easyocr

logger = logging.getLogger(__name__)


class OCRService:
    """Serviço para reconhecimento de placas usando EasyOCR."""
    
    def __init__(self):
        self.confidence_threshold = 0.6
        self.reader = None
        self._initialize_easyocr()
        
    def _initialize_easyocr(self):
        """Inicializa o EasyOCR reader."""
        try:
            logger.info("Inicializando EasyOCR...")
            # Configurar EasyOCR para português e inglês
            self.reader = easyocr.Reader(['pt', 'en'], gpu=True)
            logger.info("EasyOCR inicializado com sucesso")
        except Exception as e:
            logger.error(f"Erro ao inicializar EasyOCR: {e}")
            logger.info("Tentando inicializar EasyOCR sem GPU...")
            try:
                self.reader = easyocr.Reader(['pt', 'en'], gpu=False)
                logger.info("EasyOCR inicializado sem GPU")
            except Exception as e2:
                logger.error(f"Erro crítico ao inicializar EasyOCR: {e2}")
                self.reader = None
        
    async def detect_plate(self, image_base64: str) -> Optional[Dict]:
        """
        Detecta placa em uma imagem base64 usando EasyOCR.
        
        Args:
            image_base64: Imagem da região da placa codificada em base64
            
        Returns:
            Dict com 'plate' e 'confidence' ou None se não detectar
        """
        try:
            logger.info("Iniciando detecção de placa via EasyOCR")
            
            if self.reader is None:
                logger.error("EasyOCR não foi inicializado corretamente")
                return None
            
            image_array = self._base64_to_numpy(image_base64)
            if image_array is None:
                return None
            
            result = await self._process_with_easyocr(image_array)
            
            if result and result.get('plate'):
                plate = self._clean_plate_text(result['plate'])
                if self._is_valid_brazilian_plate(plate):
                    logger.info(f"Placa válida detectada: {plate}")
                    return {
                        'plate': plate,
                        'confidence': result.get('confidence', 0.0)
                    }
                else:
                    logger.warning(f"Placa detectada não está em formato válido: {result['plate']}")
            
            return None
            
        except Exception as e:
            logger.error(f"Erro na detecção de placa: {e}")
            return None

    def _base64_to_numpy(self, image_base64: str) -> Optional[np.ndarray]:
        """Converte base64 para array numpy."""
        try:
            # Remover prefixo data:image se presente
            if ',' in image_base64:
                image_base64 = image_base64.split(',')[1]
            
            # Decodificar base64
            image_data = base64.b64decode(image_base64)
            
            # Converter para array numpy
            nparr = np.frombuffer(image_data, np.uint8)
            
            # Decodificar imagem
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if image is None:
                logger.error("Falha ao decodificar imagem")
                return None
                
            return image
            
        except Exception as e:
            logger.error(f"Erro ao converter base64 para numpy: {e}")
            return None

    async def _process_with_easyocr(self, image_array: np.ndarray) -> Optional[Dict]:
        """
        Processa imagem com EasyOCR para detectar texto da placa.
        
        Args:
            image_array: Array numpy da imagem da placa
            
        Returns:
            Dict com texto e confiança detectados
        """
        try:
            logger.debug("Processando imagem com EasyOCR...")
            
            # Executar EasyOCR
            results = self.reader.readtext(image_array)
            
            if not results:
                logger.warning("EasyOCR não detectou nenhum texto")
                return None
            
            # Processar resultados e encontrar o texto mais provável da placa
            best_result = self._find_best_plate_text(results)
            
            if best_result:
                logger.info(f"EasyOCR detectou: {best_result['text']} (confiança: {best_result['confidence']:.2f})")
                return {
                    'plate': best_result['text'],
                    'confidence': best_result['confidence']
                }
            
            return None
            
        except Exception as e:
            logger.error(f"Erro no processamento EasyOCR: {e}")
            return None

    def _find_best_plate_text(self, ocr_results: list) -> Optional[Dict]:
        """
        Encontra o melhor candidato a placa nos resultados do EasyOCR.
        
        Args:
            ocr_results: Lista de resultados do EasyOCR [(bbox, text, confidence), ...]
            
        Returns:
            Melhor candidato com texto e confiança
        """
        try:
            plate_candidates = []
            
            for (bbox, text, confidence) in ocr_results:
                # Filtrar por confiança mínima
                if confidence < self.confidence_threshold:
                    continue
                
                # Limpar texto
                cleaned_text = self._clean_plate_text(text)
                
                # Verificar se parece com uma placa brasileira
                if self._could_be_plate_text(cleaned_text):
                    plate_candidates.append({
                        'text': cleaned_text,
                        'confidence': confidence,
                        'original_text': text
                    })
            
            if not plate_candidates:
                logger.warning("Nenhum candidato válido encontrado")
                return None
            
            # Retornar candidato com maior confiança
            best_candidate = max(plate_candidates, key=lambda x: x['confidence'])
            
            logger.debug(f"Melhor candidato: {best_candidate}")
            return best_candidate
            
        except Exception as e:
            logger.error(f"Erro ao processar candidatos: {e}")
            return None

    def _could_be_plate_text(self, text: str) -> bool:
        """
        Verifica se o texto poderia ser uma placa brasileira.
        Mais permissivo que _is_valid_brazilian_plate.
        
        Args:
            text: Texto limpo
            
        Returns:
            True se poderia ser uma placa
        """
        if not text or len(text) < 6 or len(text) > 8:
            return False
        
        # Deve conter pelo menos letras e números
        has_letters = any(c.isalpha() for c in text)
        has_numbers = any(c.isdigit() for c in text)
        
        if not (has_letters and has_numbers):
            return False
        
        # Se tem 7 caracteres, verificar formato básico
        if len(text) == 7:
            # Deve começar com pelo menos 2 letras
            if not (text[0].isalpha() and text[1].isalpha()):
                return False
        
        return True

    def _clean_plate_text(self, raw_text: str) -> str:
        """
        Limpa e formata o texto da placa detectada.
        """
        cleaned = re.sub(r'[^A-Z0-9]', '', raw_text.upper())
        return cleaned

    def _is_valid_brazilian_plate(self, plate: str) -> bool:
        """
        Valida se a placa está no formato brasileiro válido.
        
        Formatos aceitos:
        - Formato antigo: ABC1234 (3 letras + 4 números)
        - Formato Mercosul: ABC1A23 (3 letras + 1 número + 1 letra + 2 números)
        """
        if not plate or len(plate) != 7:
            return False
        
        # Formato antigo: ABC1234
        old_format = re.match(r'^[A-Z]{3}[0-9]{4}$', plate)
        
        # Formato Mercosul: ABC1A23
        mercosul_format = re.match(r'^[A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2}$', plate)
        
        return old_format is not None or mercosul_format is not None

    async def test_ocr_performance(self, test_images: list) -> Dict:
        """
        Testa performance do OCR com múltiplas imagens.
        
        Args:
            test_images: Lista de imagens base64 para teste
            
        Returns:
            Estatísticas de performance
        """
        results = {
            'total_images': len(test_images),
            'successful_detections': 0,
            'failed_detections': 0,
            'average_confidence': 0.0,
            'detected_plates': []
        }
        
        total_confidence = 0.0
        
        for i, image_base64 in enumerate(test_images):
            try:
                logger.info(f"Testando imagem {i+1}/{len(test_images)}")
                
                result = await self.detect_plate(image_base64)
                
                if result:
                    results['successful_detections'] += 1
                    results['detected_plates'].append({
                        'image_index': i,
                        'plate': result['plate'],
                        'confidence': result['confidence']
                    })
                    total_confidence += result['confidence']
                else:
                    results['failed_detections'] += 1
                    
            except Exception as e:
                logger.error(f"Erro no teste da imagem {i}: {e}")
                results['failed_detections'] += 1
        
        # Calcular estatísticas
        if results['successful_detections'] > 0:
            results['average_confidence'] = total_confidence / results['successful_detections']
        
        results['success_rate'] = results['successful_detections'] / results['total_images'] * 100
        
        logger.info(f"Teste concluído: {results['success_rate']:.1f}% de sucesso")
        return results

    def get_ocr_info(self) -> Dict:
        """
        Retorna informações sobre o estado do OCR.
        
        Returns:
            Informações de configuração e status
        """
        return {
            'ocr_engine': 'EasyOCR',
            'languages': ['pt', 'en'],
            'gpu_enabled': self.reader.device if self.reader else None,
            'confidence_threshold': self.confidence_threshold,
            'status': 'ready' if self.reader else 'error'
        }
    
    # async def _detect_with_aws_rekognition(self, image_data: bytes) -> Optional[Dict]:
    #     """
    #     Integração com AWS Rekognition - implementar se necessário.
    #     """
    #     # TODO: Implementar chamada para AWS Rekognition
    #     pass

    # async def _detect_with_google_vision(self, image_data: bytes) -> Optional[Dict]:
    #     """
    #     Integração com Google Cloud Vision - implementar se necessário.
    #     """
    #     # TODO: Implementar chamada para Google Vision
    #     pass

    # async def _detect_with_tesseract(self, image_data: bytes) -> Optional[Dict]:
    #     """
    #     Integração com Tesseract OCR local - implementar se necessário.
    #     """
    #     # TODO: Implementar processamento com Tesseract
    #     pass
