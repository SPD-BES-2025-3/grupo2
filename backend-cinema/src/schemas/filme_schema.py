from pydantic import BaseModel, Field
from typing import Optional
import uuid

class Filme(BaseModel):
    id: int
    titulo: str
    diretor: str
    duracao_minutos: int
    nota: float

class FilmeCreate(BaseModel):
    titulo: str = Field(..., example="Inception", min_length=1)
    diretor: str = Field(..., example="Christopher Nolan", min_length=1)
    duracao_minutos: int = Field(..., example=148, ge=1)
    nota: float = Field(..., example=8.8, ge=0.0, le=10.0)

class FilmeUpdate(BaseModel):
    titulo: Optional[str] = None
    diretor: Optional[str] = None
    duracao_minutos: Optional[int] = None
    nota: Optional[float] = None

class FilmeResponse(Filme):
    id: uuid.UUID

    class Config:
        from_attributes = True