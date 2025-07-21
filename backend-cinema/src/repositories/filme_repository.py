from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.filme_model import Filme
from schemas.filme_schema import FilmeCreate, FilmeUpdate
from typing import List, Optional
import uuid

class FilmeRepository:
    
    def __init__(self, db: Session):
        self.db = db
    
    def criar_filme(self, filme_data: FilmeCreate) -> Filme:
        try:
            db_filme = Filme(
                titulo=filme_data.titulo,
                diretor=filme_data.diretor,
                duracao_minutos=filme_data.duracao_minutos,
                nota=filme_data.nota
            )
            
            self.db.add(db_filme)
            self.db.commit()
            self.db.refresh(db_filme)
            
            return db_filme
            
        except SQLAlchemyError as e:
            self.db.rollback()
            raise
        except Exception as e:
            self.db.rollback()
            raise
    
    def obter_filme_por_id(self, filme_id: uuid.UUID) -> Optional[Filme]:
        return self.db.query(Filme).filter(Filme.id == filme_id).first()
    
    def obter_filme_por_titulo(self, titulo: str) -> List[Filme]:
        return self.db.query(Filme).filter(Filme.titulo.ilike(f"%{titulo}%")).all()
    
    def obter_todos_filmes(self, skip: int = 0, limit: int = 100) -> List[Filme]:
        return self.db.query(Filme).offset(skip).limit(limit).all()
    
    def atualizar_filme(self, filme_id: uuid.UUID, filme_data: FilmeUpdate) -> Optional[Filme]:
        db_filme = self.obter_filme_por_id(filme_id)
        if db_filme:
            update_data = filme_data.model_dump(exclude_unset=True)
            for campo, valor in update_data.items():
                setattr(db_filme, campo, valor)
            self.db.commit()
            self.db.refresh(db_filme)
        return db_filme
    
    def deletar_filme(self, filme_id: uuid.UUID) -> bool:
        db_filme = self.obter_filme_por_id(filme_id)
        if db_filme:
            self.db.delete(db_filme)
            self.db.commit()
            return True
        return False