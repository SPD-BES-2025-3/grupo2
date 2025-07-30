import base64
import cv2
import numpy as np
import torch
import logging
import os
from typing import Optional, List
from PIL import Image
import io
from ultralytics import YOLO

logger = logging.getLogger(__name__)


class PlateDetectionService:
    """Serviço para detecção de placas em imagens usando PyTorch."""
    
    def __init__(self):
        self.model = None
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.confidence_threshold = 0.5
        self._load_model()
        
    def _load_model(self):
        """Carrega o modelo PyTorch para detecção de placas."""
        try:
            logger.info("Carregando modelo de detecção de placas...")
            
            # Caminho para o modelo YOLOv8
            model_path = os.path.join(os.path.dirname(__file__), '..', 'plate_detector', 'LP-detection.pt')
            model_path = os.path.abspath(model_path)
            
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Modelo não encontrado em: {model_path}")
            
            # Carregar modelo YOLOv8 customizado
            self.model = YOLO(model_path)
            
            logger.info(f"Modelo YOLOv8 carregado de: {model_path}")
            logger.info(f"Dispositivo utilizado: {self.device}")
            
        except Exception as e:
            logger.error(f"Erro ao carregar modelo de detecção: {e}")
            self.model = None

    async def detect_plate_in_image(self, image_base64: str) -> Optional[str]:
        """
        Detecta placa na imagem e retorna apenas a região da placa em base64.
        
        Args:
            image_base64: Imagem completa do veículo em base64
            
        Returns:
            Base64 da região da placa detectada, ou None se não detectar
        """
        try:
            logger.info("Iniciando detecção de placa na imagem")
            
            # Converter base64 para imagem OpenCV
            cv_image = self._base64_to_cv2(image_base64)
            if cv_image is None:
                return None
            
            # Método alternativo usando YOLOv8 crop (mais eficiente)
            plate_base64 = await self._detect_and_crop_plate_yolo(cv_image)
            if plate_base64:
                return plate_base64
            
            # Fallback: método manual com bounding boxes
            bounding_boxes = await self._detect_plates(cv_image)
            
            if not bounding_boxes:
                logger.warning("Nenhuma placa detectada na imagem")
                return None
            
            # Pegar a placa com maior confiança (primeira da lista)
            best_bbox = bounding_boxes[0]
            
            # Extrair região da placa
            plate_region = self._extract_plate_region(cv_image, best_bbox)
            
            # Converter região da placa de volta para base64
            plate_base64 = self._cv2_to_base64(plate_region)
            
            logger.info(f"Placa detectada com confiança {best_bbox['confidence']:.2f}")
            return plate_base64
            
        except Exception as e:
            logger.error(f"Erro na detecção de placa: {e}")
            return None

    async def _detect_and_crop_plate_yolo(self, cv_image: np.ndarray) -> Optional[str]:
        """
        Detecta e extrai a região da placa usando funcionalidade de crop do YOLOv8.
        Baseado no exemplo fornecido.
        
        Args:
            cv_image: Imagem OpenCV
            
        Returns:
            Base64 da região da placa cropada, ou None se não detectar
        """
        try:
            if self.model is None:
                return None
            
            # Preprocessar a imagem (YOLOv8 aceita diferentes tamanhos, mas 640x640 é padrão)
            img_preprocessed = cv2.resize(cv_image, (640, 640))
            
            # Fazer inferência com o modelo YOLOv8
            results = self.model(img_preprocessed, conf=self.confidence_threshold)
            
            # Extrair as regiões cropadas (seguindo o exemplo)
            for result in results:
                if hasattr(result, 'boxes') and result.boxes is not None and len(result.boxes) > 0:
                    # Usar a funcionalidade de crop do YOLOv8
                    crops = result.crop()
                    
                    if len(crops) > 0:
                        # Pegar o primeiro crop (maior confiança)
                        license_plate_img = crops[0]
                        
                        # Redimensionar de volta considerando a escala original
                        height, width = cv_image.shape[:2]
                        scale_x = width / 640
                        scale_y = height / 640
                        
                        # Se necessário, aplicar escala no crop
                        if scale_x != 1.0 or scale_y != 1.0:
                            new_height = int(license_plate_img.shape[0] * scale_y)
                            new_width = int(license_plate_img.shape[1] * scale_x)
                            license_plate_img = cv2.resize(license_plate_img, (new_width, new_height))
                        
                        # Converter para base64
                        plate_base64 = self._cv2_to_base64(license_plate_img)
                        
                        logger.info("Placa extraída usando YOLOv8 crop")
                        return plate_base64
            
            return None
            
        except Exception as e:
            logger.error(f"Erro no crop YOLOv8: {e}")
            return None

    def _base64_to_cv2(self, image_base64: str) -> Optional[np.ndarray]:
        """Converte base64 para imagem OpenCV."""
        try:
            # Remover prefixo data:image se presente
            if ',' in image_base64:
                image_base64 = image_base64.split(',')[1]
            
            # Decodificar base64
            image_data = base64.b64decode(image_base64)
            
            # Converter para PIL Image
            pil_image = Image.open(io.BytesIO(image_data))
            
            # Converter para RGB se necessário
            if pil_image.mode != 'RGB':
                pil_image = pil_image.convert('RGB')
            
            # Converter para OpenCV (BGR)
            cv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
            
            return cv_image
            
        except Exception as e:
            logger.error(f"Erro ao converter base64 para OpenCV: {e}")
            return None

    def _cv2_to_base64(self, cv_image: np.ndarray) -> str:
        """Converte imagem OpenCV para base64."""
        try:
            _, buffer = cv2.imencode('.jpg', cv_image)
            
            image_base64 = base64.b64encode(buffer).decode('utf-8')
            
            return image_base64
            
        except Exception as e:
            logger.error(f"Erro ao converter OpenCV para base64: {e}")
            return ""

    async def _detect_plates(self, cv_image: np.ndarray) -> List[dict]:
        """
        Detecta placas na imagem usando modelo YOLOv8.
        
        Args:
            cv_image: Imagem OpenCV
            
        Returns:
            Lista de bounding boxes com coordenadas e confiança
        """
        try:
            if self.model is None:
                logger.warning("Modelo não carregado, usando simulação")
                return await self._simulate_plate_detection(cv_image)
            
            # Preprocessar a imagem para o modelo YOLOv8
            img_preprocessed = cv2.resize(cv_image, (640, 640))
            
            # Fazer inferência com o modelo YOLOv8
            results = self.model(img_preprocessed, conf=self.confidence_threshold)
            
            # Processar resultados
            bounding_boxes = []
            
            for result in results:
                boxes = result.boxes
                if boxes is not None and len(boxes) > 0:
                    for box in boxes:
                        # Extrair coordenadas e confiança
                        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                        confidence = float(box.conf[0].cpu().numpy())
                        
                        # Escalar coordenadas de volta para a imagem original
                        height, width = cv_image.shape[:2]
                        scale_x = width / 640
                        scale_y = height / 640
                        
                        bbox = {
                            'x1': int(x1 * scale_x),
                            'y1': int(y1 * scale_y),
                            'x2': int(x2 * scale_x),
                            'y2': int(y2 * scale_y),
                            'confidence': confidence
                        }
                        bounding_boxes.append(bbox)
            
            # Ordenar por confiança (maior primeiro)
            bounding_boxes.sort(key=lambda x: x['confidence'], reverse=True)
            
            logger.info(f"YOLOv8 detectou {len(bounding_boxes)} placas")
            return bounding_boxes
            
        except Exception as e:
            logger.error(f"Erro na detecção YOLOv8: {e}")
            return []

    async def _simulate_plate_detection(self, cv_image: np.ndarray) -> List[dict]:
        """
        Simula detecção de placa para desenvolvimento.
        Remove quando modelo real estiver disponível.
        """
        height, width = cv_image.shape[:2]
        
        # Simular que encontrou uma placa na parte inferior central da imagem
        # (posição típica de placas em fotos frontais de carros)
        simulated_bbox = {
            'x1': int(width * 0.3),    # 30% da largura
            'y1': int(height * 0.7),   # 70% da altura  
            'x2': int(width * 0.7),    # 70% da largura
            'y2': int(height * 0.9),   # 90% da altura
            'confidence': 0.85
        }
        
        logger.info("Simulação: Placa detectada na região inferior central")
        return [simulated_bbox]

    def _extract_plate_region(self, cv_image: np.ndarray, bbox: dict) -> np.ndarray:
        """Extrai região da placa da imagem completa."""
        try:
            x1, y1, x2, y2 = bbox['x1'], bbox['y1'], bbox['x2'], bbox['y2']
            
            # Adicionar margem pequena ao redor da placa
            margin = 10
            height, width = cv_image.shape[:2]
            
            x1 = max(0, x1 - margin)
            y1 = max(0, y1 - margin) 
            x2 = min(width, x2 + margin)
            y2 = min(height, y2 + margin)
            
            # Extrair região
            plate_region = cv_image[y1:y2, x1:x2]
            
            logger.debug(f"Região da placa extraída: {plate_region.shape}")
            return plate_region
            
        except Exception as e:
            logger.error(f"Erro ao extrair região da placa: {e}")
            return cv_image

    def _cv2_to_tensor(self, cv_image: np.ndarray) -> torch.Tensor:
        """Converte imagem OpenCV para tensor PyTorch."""
        # Converter BGR para RGB
        rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        
        # Normalizar para [0, 1]
        image_array = rgb_image.astype(np.float32) / 255.0
        
        # Converter para tensor e ajustar dimensões [C, H, W]
        image_tensor = torch.from_numpy(image_array).permute(2, 0, 1)
        
        # Adicionar batch dimension [1, C, H, W]
        image_tensor = image_tensor.unsqueeze(0)
        
        # Mover para dispositivo (GPU/CPU)
        image_tensor = image_tensor.to(self.device)
        
        return image_tensor

    async def is_plate_detected(self, image_base64: str) -> bool:
        """
        Verifica se há placa na imagem sem extrair a região.
        Método rápido para pré-validação.
        
        Args:
            image_base64: Imagem em base64
            
        Returns:
            True se detectar placa, False caso contrário
        """
        try:
            cv_image = self._base64_to_cv2(image_base64)
            if cv_image is None:
                return False
            
            bounding_boxes = await self._detect_plates(cv_image)
            return len(bounding_boxes) > 0
            
        except Exception as e:
            logger.error(f"Erro na verificação de placa: {e}")
            return False
