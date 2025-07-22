from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.sessao_model import Sessao
from schemas.sessao_schema import SessaoCreate, SessaoUpdate
from typing import List, Optional
import uuid

class SessaoRepository:
    
    def __init__(self, db: Session):
        self.db = db
    
    def criar_sessao(self, sessao_data: SessaoCreate) -> Sessao:
        try:
            db_sessao = Sessao(
                filme_id=sessao_data.filme_id,
                data=sessao_data.data,
                hora=sessao_data.hora,
                preco_por_veiculo=sessao_data.preco_por_veiculo
            )
            
            self.db.add(db_sessao)
            self.db.commit()
            self.db.refresh(db_sessao)
            
            return db_sessao
            
        except SQLAlchemyError as e:
            self.db.rollback()
            raise
        except Exception as e:
            self.db.rollback()
            raise
    
    def obter_sessao_por_id(self, sessao_id: uuid.UUID) -> Optional[Sessao]:
        return self.db.query(Sessao).filter(Sessao.id == sessao_id).first()
    
    def obter_sessoes_por_filme(self, filme_id: uuid.UUID) -> List[Sessao]:
        return self.db.query(Sessao).filter(Sessao.filme_id == filme_id).all()
    
    def obter_todas_sessoes(self, skip: int = 0, limit: int = 100) -> List[Sessao]:
        return self.db.query(Sessao).offset(skip).limit(limit).all()
    
    def atualizar_sessao(self, sessao_id: uuid.UUID, sessao_data: SessaoUpdate) -> Optional[Sessao]:
        db_sessao = self.obter_sessao_por_id(sessao_id)
        if db_sessao:
            update_data = sessao_data.model_dump(exclude_unset=True)
            for campo, valor in update_data.items():
                setattr(db_sessao, campo, valor)
            self.db.commit()
            return db_sessao
        return None
    
    def excluir_sessao(self, sessao_id: uuid.UUID) -> bool:
        db_sessao = self.obter_sessao_por_id(sessao_id)
        if db_sessao:
            self.db.delete(db_sessao)
            self.db.commit()
            return True
        return False
    