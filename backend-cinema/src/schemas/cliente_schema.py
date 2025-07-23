from pydantic import BaseModel
from typing import Optional
import uuid

class ClienteBase(BaseModel):
    nome: str
    email: str
    placa: str

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    placa: Optional[str] = None

class ClienteResponse(ClienteBase):
    id: uuid.UUID
    
    class Config:
        from_attributes = True  # Para compatibilidade com SQLAlchemy
