from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from config.database import Base

class Cliente(Base):

    __tablename__ = "clientes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    placa = Column(String(10), nullable=False)
    
    def __repr__(self):
        return f"<Cliente(id={self.id}, nome='{self.nome}', email='{self.email}', placa='{self.placa}')>"
