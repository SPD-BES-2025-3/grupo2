from sqlalchemy import Column, Integer, Float, Enum, ARRAY, Date, Time
from sqlalchemy.dialects.postgresql import UUID
import uuid
from config.database import Base

class Sessao(Base):

    __tablename__ = "sessoes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    filme_id = Column(UUID(as_uuid=True), nullable=False)   
    data = Column(Date, nullable=False) 
    hora = Column(Time, nullable=False) 
    preco_por_veiculo = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Sessao(id={self.id}, filme_id={self.filme_id}, data='{self.data}', hora='{self.hora}', preco_por_veiculo={self.preco_por_veiculo})>"