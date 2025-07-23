from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid

from config.database import get_db
from repositories.sessao_repository import SessaoRepository
from repositories.filme_repository import FilmeRepository
from services.sessao_service import SessaoService
from schemas.sessao_schema import SessaoCreate, SessaoUpdate, SessaoResponse

router = APIRouter(
    prefix="/sessoes",
    tags=["sessoes"]
)

def get_sessao_service(
    db: Session = Depends(get_db)
) -> SessaoService:
    sessao_repository = SessaoRepository(db)
    filme_repository = FilmeRepository(db)
    return SessaoService(sessao_repository, filme_repository)

@router.post("/", response_model=SessaoResponse, status_code=status.HTTP_201_CREATED)
def criar_sessao(
    sessao_data: SessaoCreate,
    sessao_service: SessaoService = Depends(get_sessao_service)
):
    try:
        return sessao_service.criar_sessao(sessao_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    
@router.get("/", response_model=List[SessaoResponse])
def listar_sessoes(
    skip: int = 0,
    limit: int = 100,
    sessao_service: SessaoService = Depends(get_sessao_service)
):
    return sessao_service.obter_todas_sessoes(skip=skip, limit=limit)

@router.get("/{sessao_id}", response_model=SessaoResponse)
def obter_sessao(
    sessao_id: uuid.UUID,
    sessao_service: SessaoService = Depends(get_sessao_service)
):
    sessao = sessao_service.obter_sessao_por_id(sessao_id)
    if not sessao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sessão não encontrada"
        )
    return sessao

@router.get("/filme/{filme_id}", response_model=List[SessaoResponse])
def obter_sessoes_por_filme(
    filme_id: uuid.UUID,
    sessao_service: SessaoService = Depends(get_sessao_service)
):
    sessoes = sessao_service.obter_sessoes_por_filme(filme_id)
    if not sessoes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhuma sessão encontrada para este filme"
        )
    return sessoes

@router.put("/{sessao_id}", response_model=SessaoResponse)
def atualizar_sessao(
    sessao_id: uuid.UUID,
    sessao_data: SessaoUpdate,
    sessao_service: SessaoService = Depends(get_sessao_service)
):
    try:
        sessao = sessao_service.atualizar_sessao(sessao_id, sessao_data)
        if not sessao:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Sessão não encontrada"
            )
        return sessao
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    
@router.delete("/{sessao_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_sessao(
    sessao_id: uuid.UUID,
    sessao_service: SessaoService = Depends(get_sessao_service)
):
    if not sessao_service.excluir_sessao(sessao_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sessão não encontrada"
        )

