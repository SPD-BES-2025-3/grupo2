from datetime import date, time
from pydantic import BaseModel, Field
from typing import List, Optional
from utils.enums import GeneroEnum
import uuid

class SessaoBase(BaseModel):
    filme_id: uuid.UUID
    data: date
    hora: time
    preco_por_veiculo: int


class SessaoCreate(BaseModel):
    filme_id: uuid.UUID = Field(..., description="ID do filme associado à sessão")
    data: date = Field(..., description="Data da sessão no formato YYYY-MM-DD")
    hora: time = Field(..., description="Hora da sessão no formato HH:MM")   
    preco_por_veiculo: int = Field(..., ge=0, description="Preço por veículo para a sessão")

class SessaoUpdate(BaseModel):
    filme_id: Optional[uuid.UUID] = Field(None, description="ID do filme associado à sessão")
    data: Optional[date] = Field(None, description="Data da sessão no formato YYYY-MM-DD")
    hora: Optional[time] = Field(None, description="Hora da sessão no formato HH:MM")
    preco_por_veiculo: Optional[int] = Field(None, ge=0, description="Preço por veículo para a sessão")
   
class SessaoResponse(SessaoBase):
    id: uuid.UUID

    class Config:
        from_attributes = True


