from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class PlateEventType(str, Enum):
    PLATE_DETECTED = "plate_detected"
    PLATE_PROCESSED = "plate_processed"
    PLATE_MATCHED = "plate_matched"
    PLATE_NOT_FOUND = "plate_not_found"
    ACCESS_GRANTED = "access_granted"
    ACCESS_DENIED = "access_denied"


class PlateImageEvent(BaseModel):
    """Evento de recebimento de imagem de placa via MQTT."""
    id: Optional[str] = Field(None, description="ID único do evento")
    gate_id: str = Field(..., description="ID da catraca que capturou a imagem")
    event_type: PlateEventType = Field(..., description="Tipo do evento")
    
    image_base64: Optional[str] = Field(None, description="Imagem em base64")
    image_url: Optional[str] = Field(None, description="URL da imagem")
    image_path: Optional[str] = Field(None, description="Caminho local da imagem")
    
    detected_plate: Optional[str] = Field(None, description="Placa detectada pelo OCR")
    confidence_score: Optional[float] = Field(None, description="Confiança da detecção (0-1)")
    
    session_id: Optional[int] = Field(None, description="ID da sessão relacionada")
    reservation_id: Optional[int] = Field(None, description="ID da reserva encontrada")
    
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp do evento")
    processing_time_ms: Optional[int] = Field(None, description="Tempo de processamento em ms")
    
    camera_metadata: Optional[dict] = Field(None, description="Metadados da câmera")
    
    class Config:
        allow_population_by_field_name = True
        populate_by_name = True
