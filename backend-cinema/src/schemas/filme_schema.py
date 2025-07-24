from pydantic import BaseModel, Field
from typing import List, Optional
from models.filme_model import GeneroEnum, ClassificacaoIndicativaEnum
import uuid

class FilmeBase(BaseModel):
    titulo: str
    diretor: str
    generos: List[GeneroEnum]
    duracao_minutos: int
    classificacao_indicativa: ClassificacaoIndicativaEnum

class FilmeCreate(BaseModel):
    titulo: str = Field(..., example="Inception", min_length=1)
    diretor: str = Field(..., example="Christopher Nolan", min_length=1)
    generos: list[GeneroEnum] = Field(..., example=["Ficção científica", "Ação"])
    duracao_minutos: int = Field(..., example=148, ge=1)
    classificacao_indicativa: ClassificacaoIndicativaEnum = Field(..., example="14")

class FilmeUpdate(BaseModel):
    titulo: Optional[str] = None
    diretor: Optional[str] = None
    generos: Optional[List[GeneroEnum]] = None
    duracao_minutos: Optional[int] = None
    classificacao_indicativa: Optional[ClassificacaoIndicativaEnum] = None

class FilmeResponse(FilmeBase):
    id: uuid.UUID

    class Config:
        from_attributes = True