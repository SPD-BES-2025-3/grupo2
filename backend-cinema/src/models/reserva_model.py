import uuid

from beanie import Document
from pydantic import Field

from utils.enums import StatusReservaEnum

class Reserva(Document):
    sessao_id: uuid.UUID = Field(..., description="ID da sessão (referência ao PostgreSQL)")
    cliente_id: uuid.UUID = Field(..., description="ID do cliente que está fazendo a reserva")
    status: StatusReservaEnum = Field(default=StatusReservaEnum.PENDENTE, description="Status da reserva")

    class Settings:
        name = "reservas"  # Nome da collection no MongoDB
