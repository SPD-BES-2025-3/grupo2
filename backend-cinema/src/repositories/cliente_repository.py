from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.cliente_model import Cliente
from schemas.cliente_schema import ClienteCreate, ClienteUpdate
from typing import List, Optional
import uuid

class ClienteRepository:
    
    def __init__(self, db: Session):
        self.db = db
    
    def criar_cliente(self, cliente_data: ClienteCreate) -> Cliente:

        try:
            
            db_cliente = Cliente(
                nome=cliente_data.nome,
                email=cliente_data.email,
                placa=cliente_data.placa
            )
            
            self.db.add(db_cliente)
            
            self.db.commit()
            
            self.db.refresh(db_cliente)
            
            return db_cliente
            
        except SQLAlchemyError as e:
            self.db.rollback()
            raise
        except Exception as e:
            self.db.rollback()
            raise
    
    def obter_cliente_por_id(self, cliente_id: uuid.UUID) -> Optional[Cliente]:
        return self.db.query(Cliente).filter(Cliente.id == cliente_id).first()
    
    def obter_cliente_por_email(self, email: str) -> Optional[Cliente]:
        return self.db.query(Cliente).filter(Cliente.email == email).first()
    
    def obter_todos_clientes(self, skip: int = 0, limit: int = 100) -> List[Cliente]:
        return self.db.query(Cliente).offset(skip).limit(limit).all()
    
    def atualizar_cliente(self, cliente_id: uuid.UUID, cliente_data: ClienteUpdate) -> Optional[Cliente]:
        db_cliente = self.obter_cliente_por_id(cliente_id)
        if db_cliente:
            update_data = cliente_data.model_dump(exclude_unset=True)
            for campo, valor in update_data.items():
                setattr(db_cliente, campo, valor)
            self.db.commit()
            self.db.refresh(db_cliente)
        return db_cliente
    
    def deletar_cliente(self, cliente_id: uuid.UUID) -> bool:
        db_cliente = self.obter_cliente_por_id(cliente_id)
        if db_cliente:
            self.db.delete(db_cliente)
            self.db.commit()
            return True
        return False
