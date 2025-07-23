from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid

from config.database import get_db
from repositories.filme_repository import FilmeRepository
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
    try:
        return filme_service.criar_filme(filme_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

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

@router.get("/titulo/{titulo}", response_model=List[FilmeResponse])
def obter_filme_por_titulo(
    titulo: str,
    filme_service: FilmeService = Depends(get_filme_service)
):
    filmes = filme_service.obter_filme_por_titulo(titulo)
    if not filmes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum filme encontrado com esse título"
        )
    return filmes

@router.put("/{filme_id}", response_model=FilmeResponse)
def atualizar_filme(
    filme_id: uuid.UUID,
    filme_data: FilmeUpdate,
    filme_service: FilmeService = Depends(get_filme_service)
):
    try:
        filme = filme_service.atualizar_filme(filme_id, filme_data)
        if not filme:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Filme não encontrado"
            )
        return filme
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.delete("/{filme_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_filme(
    filme_id: uuid.UUID,
    filme_service: FilmeService = Depends(get_filme_service)
):
    if not filme_service.deletar_filme(filme_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado"
        )

# Endpoint para exibir os gêneros de um filme
@router.get("/{filme_id}/generos", response_model=List[str])
def obter_generos_filme(
    filme_id: uuid.UUID,
    filme_service: FilmeService = Depends(get_filme_service)
):
    generos = filme_service.obter_generos_filme(filme_id)
    if not generos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado ou sem gêneros"
        )
    return generos
