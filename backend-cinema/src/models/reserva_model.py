import uuid
from datetime import datetime
from enum import Enum
from typing import Optional

from beanie import Document
from pydantic import Field

class StatusReservaEnum(str, Enum):
    """Enum para status de reserva"""
    PENDENTE = "pendente"
    CONFIRMADA = "confirmada"
    CANCELADA = "cancelada"
    FINALIZADA = "finalizada"

class Reserva(Document):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    sessao_id: str
    cliente_id: str
    status: StatusReservaEnum = StatusReservaEnum.PENDENTE
    data_reserva: datetime = Field(default_factory=datetime.now)
    
    class Settings:
        name = "reservas"
        
    class Config:
        use_enum_values = True
