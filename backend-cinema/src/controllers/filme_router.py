from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid

from config.database import get_db
from repositories.cliente_repository import FilmeRepository
from services.filme_service import FilmeService
from schemas.filme_schema import FilmeCreate, FilmeUpdate, FilmeResponse

router = APIRouter(
    prefix="/filmes",
    tags=["filmes"]
)

def get_filme_service(db: Session = Depends(get_db)) -> FilmeService:
    filme_repository = FilmeRepository(db)
    return FilmeService(filme_repository)

@router.post("/", response_model=FilmeResponse, status_code=status.HTTP_201_CREATED)
def criar_filme(    
    filme_data: FilmeCreate,
    filme_service: FilmeService = Depends(get_filme_service)
):
    return filme_service.criar_filme(filme_data)

@router.get("/", response_model=List[FilmeResponse])
def listar_filmes(
    skip: int = 0,
    limit: int = 100,
    filme_service: FilmeService = Depends(get_filme_service)
):
    return filme_service.obter_todos_filmes(skip=skip, limit=limit)

@router.get("/{filme_id}", response_model=FilmeResponse)
def obter_filme(
    filme_id: uuid.UUID,
    filme_service: FilmeService = Depends(get_filme_service)
):
    filme = filme_service.obter_filme_por_id(filme_id)
    if not filme:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado"
        )
    return filme

@router.put("/{filme_id}", response_model=FilmeResponse)
def atualizar_filme(
    filme_id: uuid.UUID,
    filme_data: FilmeUpdate,
    filme_service: FilmeService = Depends(get_filme_service)
):
    try:
        return filme_service.atualizar_filme(filme_id, filme_data)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao atualizar filme"
        )

@router.delete("/{filme_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_filme(
    filme_id: uuid.UUID,
    filme_service: FilmeService = Depends(get_filme_service)
):
    try:
        filme_service.deletar_filme(filme_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao deletar filme"
        )
