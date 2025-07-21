from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid

from config.database import get_db
from repositories.cliente_repository import ClienteRepository
from services.cliente_service import ClienteService
from schemas.cliente_schema import ClienteCreate, ClienteUpdate, ClienteResponse

router = APIRouter(
    prefix="/clientes",
    tags=["clientes"]
)

def get_cliente_service(db: Session = Depends(get_db)) -> ClienteService:

    cliente_repository = ClienteRepository(db)
    return ClienteService(cliente_repository)

@router.post("/", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
def criar_cliente(
    cliente_data: ClienteCreate,
    cliente_service: ClienteService = Depends(get_cliente_service)
):

    try:
        return cliente_service.criar_cliente(cliente_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/", response_model=List[ClienteResponse])
def listar_clientes(
    skip: int = 0,
    limit: int = 100,
    cliente_service: ClienteService = Depends(get_cliente_service)
):

    return cliente_service.obter_todos_clientes(skip=skip, limit=limit)

@router.get("/{cliente_id}", response_model=ClienteResponse)
def obter_cliente(
    cliente_id: uuid.UUID,
    cliente_service: ClienteService = Depends(get_cliente_service)
):

    cliente = cliente_service.obter_cliente_por_id(cliente_id)
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )
    return cliente

@router.put("/{cliente_id}", response_model=ClienteResponse)
def atualizar_cliente(
    cliente_id: uuid.UUID,
    cliente_data: ClienteUpdate,
    cliente_service: ClienteService = Depends(get_cliente_service)
):

    try:
        cliente = cliente_service.atualizar_cliente(cliente_id, cliente_data)
        if not cliente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cliente não encontrado"
            )
        return cliente
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_cliente(
    cliente_id: uuid.UUID,
    cliente_service: ClienteService = Depends(get_cliente_service)
):

    if not cliente_service.deletar_cliente(cliente_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )
