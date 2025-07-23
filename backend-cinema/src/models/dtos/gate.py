from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class GateStatus(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    MAINTENANCE = "maintenance"


class Gate(BaseModel):
    """Modelo de Catraca/Portão do Cinema Drive-In."""
    id: str = Field(..., description="ID único da catraca")
    name: str = Field(..., description="Nome/descrição da catraca")
    location: str = Field(..., description="Localização física da catraca")
    status: GateStatus = Field(GateStatus.ONLINE, description="Status operacional")
    is_active: bool = Field(True, description="Se a catraca está ativa")
    
    has_camera: bool = Field(True, description="Se possui câmera para leitura de placas")
    camera_ip: Optional[str] = Field(None, description="IP da câmera")
    max_processing_time_seconds: int = Field(30, description="Tempo máximo para processar entrada")
    
    last_heartbeat: Optional[datetime] = Field(None, description="Último sinal de vida")
    total_vehicles_processed: int = Field(0, description="Total de veículos processados")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(None)
    
    class Config:
        from_attributes = True
