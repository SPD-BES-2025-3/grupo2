from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.dialects.postgresql import UUID
import uuid
from config.database import Base

class Filme(Base):

    __tablename__ = "filmes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    titulo = Column(String(100), nullable=False)
    diretor = Column(String(100), nullable=False)
    duracao_minutos = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)
    
    def __repr__(self):
        return f"<Filme(id={self.id}, titulo='{self.titulo}', diretor='{self.diretor}', duracao_minutos={self.duracao_minutos}, nota={self.nota})>"

