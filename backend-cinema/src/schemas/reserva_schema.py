import uuid
from typing import Optional

from beanie import PydanticObjectId
from pydantic import BaseModel, Field

from utils.enums import StatusReservaEnum

class ReservaBase(BaseModel):
    sessao_id: uuid.UUID = Field(..., description="ID da sessão para a qual a reserva está sendo feita")
    cliente_id: uuid.UUID = Field(..., description="ID do cliente que está fazendo a reserva")
    status: StatusReservaEnum = Field(..., description="Status atual da reserva")


class ReservaCreate(BaseModel):
    sessao_id: uuid.UUID = Field(..., description="ID da sessão para a qual a reserva está sendo feita")
    cliente_id: uuid.UUID = Field(..., description="ID do cliente que está fazendo a reserva")


class ReservaUpdate(BaseModel):
    status: Optional[StatusReservaEnum] = Field(None, description="Novo status da reserva")


class ReservaResponse(ReservaBase):
    id: PydanticObjectId = Field(..., description="ID único da reserva no MongoDB")

    class Config:
        from_attributes = True
        json_encoders = {PydanticObjectId: str}  # Para serializar o ObjectId para string no JSON
