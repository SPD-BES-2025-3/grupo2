from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class PlateEventType(str, Enum):
    """Tipos de eventos relacionados apenas ao processamento da placa."""
    PLATE_DETECTED = "plate_detected"    # Placa foi detectada na imagem
    PLATE_NOT_DETECTED = "plate_not_detected"  # Não foi possível detectar placa
    PLATE_MATCHED = "plate_matched"      # Placa encontrada no sistema
    PLATE_NOT_FOUND = "plate_not_found"  # Placa não encontrada no sistema


class PlateImageEvent(BaseModel):
    """Evento de recebimento de imagem de placa via MQTT.
    
    Compatível com os modelos Reserva (MongoDB) e Sessao (PostgreSQL).
    Todos os IDs são strings representando UUIDs para manter compatibilidade.
    """
    id: Optional[str] = Field(None, description="ID único do evento")
    gate_id: str = Field(..., description="ID da catraca que capturou a imagem")
    event_type: PlateEventType = Field(..., description="Tipo do evento")
    
    # Dados da imagem
    image_base64: Optional[str] = Field(None, description="Imagem em base64")
    
    # Resultado do OCR
    detected_plate: Optional[str] = Field(None, description="Placa detectada pelo OCR")
    confidence_score: Optional[float] = Field(None, description="Confiança da detecção (0-1)", ge=0.0, le=1.0)
    
    # Relacionamentos com outros modelos (todos como string/UUID)
    session_id: Optional[str] = Field(None, description="ID da sessão relacionada (UUID)")
    reservation_id: Optional[str] = Field(None, description="ID da reserva encontrada (UUID)")
    cliente_id: Optional[str] = Field(None, description="ID do cliente relacionado (UUID)")
    
    # Status da reserva (para compatibilidade)
    reservation_status: Optional[str] = Field(None, description="Status da reserva (pendente/confirmada/cancelada)")
    
    # Metadados temporais
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp do evento")
    processing_time_ms: Optional[int] = Field(None, description="Tempo de processamento em ms", ge=0)
    
    # Metadados adicionais
    camera_metadata: Optional[dict] = Field(None, description="Metadados da câmera")
    error_message: Optional[str] = Field(None, description="Mensagem de erro se houver")
