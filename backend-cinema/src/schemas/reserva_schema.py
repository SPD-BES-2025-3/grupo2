from datetime import datetime
from pydantic import BaseModel, Field
from models.reserva_model import StatusReservaEnum

class ReservaBase(BaseModel):
    sessao_id: str = Field(..., description="ID da sessão para a qual a reserva está sendo feita")
    cliente_id: str = Field(..., description="ID do cliente que está fazendo a reserva")

class ReservaCreate(BaseModel):
    sessao_id: str = Field(..., description="ID da sessão para a qual a reserva está sendo feita")
    cliente_id: str = Field(..., description="ID do cliente que está fazendo a reserva")
    placa: str = Field(..., description="Placa do veículo do cliente")

class ReservaUpdate(BaseModel):
    status: StatusReservaEnum

class ReservaResponse(ReservaBase):
    id: str = Field(..., description="ID único da reserva no MongoDB")
    placa: str = Field(..., description="Placa do veículo do cliente")
    status: StatusReservaEnum
    data_reserva: datetime
    
    class Config:
        from_attributes = True
