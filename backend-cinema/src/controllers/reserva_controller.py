from fastapi import APIRouter, HTTPException, Depends, status, Query
from typing import List
from services.reserva_service import ReservaService
from repositories.reserva_repository import ReservaRepository
from repositories.cliente_repository import ClienteRepository
from repositories.sessao_repository import SessaoRepository
from schemas.reserva_schema import ReservaCreate, ReservaResponse
from models.reserva_model import StatusReservaEnum

router = APIRouter(prefix="/reservas", tags=["reservas"])

def get_reserva_service() -> ReservaService:
    """Dependency injection para ReservaService"""
    return ReservaService(
        ReservaRepository(),
        ClienteRepository(),
        SessaoRepository()
    )

@router.post("/", response_model=ReservaResponse, status_code=status.HTTP_201_CREATED)
async def criar_reserva(
    reserva_data: ReservaCreate,
    service: ReservaService = Depends(get_reserva_service)
):
    """Cria uma nova reserva"""
    try:
        return await service.criar_reserva(reserva_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro interno do servidor")

@router.get("/", response_model=List[ReservaResponse])
async def listar_reservas(
    service: ReservaService = Depends(get_reserva_service)
):
    """Lista todas as reservas"""
    try:
        return await service.listar_reservas()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro interno do servidor")

@router.get("/{reserva_id}", response_model=ReservaResponse)
async def obter_reserva(
    reserva_id: str,
    service: ReservaService = Depends(get_reserva_service)
):
    """Busca uma reserva por ID"""
    try:
        reserva = await service.obter_reserva_por_id(reserva_id)
        if not reserva:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reserva não encontrada")
        return reserva
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro interno do servidor")

@router.get("/cliente/{cliente_id}", response_model=List[ReservaResponse])
async def listar_reservas_por_cliente(
    cliente_id: str,
    service: ReservaService = Depends(get_reserva_service)
):
    """Lista reservas de um cliente específico"""
    try:
        return await service.listar_reservas_por_cliente(cliente_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro interno do servidor")

@router.get("/sessao/{sessao_id}", response_model=List[ReservaResponse])
async def listar_reservas_por_sessao(
    sessao_id: str,
    service: ReservaService = Depends(get_reserva_service)
):
    """Lista reservas de uma sessão específica"""
    try:
        return await service.listar_reservas_por_sessao(sessao_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro interno do servidor")

@router.patch("/{reserva_id}/confirmar", response_model=ReservaResponse)
async def confirmar_reserva(
    reserva_id: str,
    service: ReservaService = Depends(get_reserva_service)
):
    """Confirma uma reserva"""
    try:
        reserva = await service.confirmar_reserva(reserva_id)
        if not reserva:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reserva não encontrada")
        return reserva
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro interno do servidor")

@router.patch("/{reserva_id}/cancelar", response_model=ReservaResponse)
async def cancelar_reserva(
    reserva_id: str,
    service: ReservaService = Depends(get_reserva_service)
):
    """Cancela uma reserva"""
    try:
        reserva = await service.cancelar_reserva(reserva_id)
        if not reserva:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reserva não encontrada")
        return reserva
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro interno do servidor")

@router.delete("/{reserva_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_reserva(
    reserva_id: str,
    service: ReservaService = Depends(get_reserva_service)
):
    """Deleta uma reserva permanentemente"""
    try:
        sucesso = await service.deletar_reserva(reserva_id)
        if not sucesso:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reserva não encontrada")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro interno do servidor")
