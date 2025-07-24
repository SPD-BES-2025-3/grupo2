from sqlalchemy import Column, String, Integer, Enum, ARRAY
from sqlalchemy.dialects.postgresql import UUID
import uuid
from enum import Enum as PyEnum
from config.database import Base

class ClassificacaoIndicativaEnum(str, PyEnum):
    LIVRE = "L"
    DEZ_ANOS = "10"
    DOZE_ANOS = "12"
    QUATORZE_ANOS = "14"
    DEZESSEIS_ANOS = "16"
    DEZOITO_ANOS = "18"

    def __str__(self):
        return str(self.value)

class GeneroEnum(str, PyEnum):
    ACAO = "Ação"
    AVENTURA = "Aventura"
    ANIMACAO = "Animação"
    ANIME = "Anime"
    BIOGRAFIA = "Biografia"
    COMEDIA = "Comédia"
    DANCA = "Dança"
    DOCUMENTARIO = "Documentário"
    DRAMA = "Drama"
    ESPIONAGEM = "Espionagem"
    FAROESTE = "Faroeste"
    FANTASIA = "Fantasia"
    FICCAO_CIENTIFICA = "Ficção científica"
    MUSICAL = "Musical"
    FILME_POLICIAL = "Filme policial"
    TERROR = "Terror"
    ROMANCE = "Romance"
    SUSPENSE = "Suspense"


class Filme(Base):

    __tablename__ = "filmes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    titulo = Column(String(100), nullable=False)
    diretor = Column(String(100), nullable=False)
    generos = Column(ARRAY(String), nullable=False)
    duracao_minutos = Column(Integer, nullable=False)
    classificacao_indicativa = Column(Enum(ClassificacaoIndicativaEnum), nullable=False)
    
    def __repr__(self):
        return f"<Filme(id={self.id}, titulo='{self.titulo}', generos={self.generos})>"
