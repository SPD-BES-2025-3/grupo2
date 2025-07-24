from typing import List, Optional
from repositories.reserva_repository import ReservaRepository
from repositories.cliente_repository import ClienteRepository
from repositories.sessao_repository import SessaoRepository
from schemas.reserva_schema import ReservaCreate, ReservaUpdate, ReservaResponse
from models.reserva_model import StatusReservaEnum
from utils.validators import validar_status_reserva, validar_transicao_status
import uuid

class ReservaService:
    def __init__(
        self, 
        reserva_repository: ReservaRepository,
        cliente_repository: ClienteRepository,
        sessao_repository: SessaoRepository
    ):
        self.reserva_repository = reserva_repository
        self.cliente_repository = cliente_repository
        self.sessao_repository = sessao_repository

    async def criar_reserva(self, reserva_data: ReservaCreate) -> ReservaResponse:
        """Cria uma nova reserva com validações"""
        # Validar se cliente existe
        cliente = self.cliente_repository.obter_cliente_por_id(uuid.UUID(reserva_data.cliente_id))
        if not cliente:
            raise ValueError("Cliente não encontrado")
        
        # Validar se sessão existe
        sessao = self.sessao_repository.obter_sessao_por_id(uuid.UUID(reserva_data.sessao_id))
        if not sessao:
            raise ValueError("Sessão não encontrada")
        
        # Verificar se cliente já tem reserva para esta sessão
        reservas_existentes = await self.reserva_repository.listar_reservas_por_cliente(reserva_data.cliente_id)
        for reserva in reservas_existentes:
            if (reserva.sessao_id == reserva_data.sessao_id and 
                reserva.status in [StatusReservaEnum.PENDENTE, StatusReservaEnum.CONFIRMADA]):
                raise ValueError("Cliente já possui reserva para esta sessão")
        
        reserva = await self.reserva_repository.criar_reserva(reserva_data)
        return ReservaResponse.model_validate(reserva.model_dump())

    async def obter_reserva_por_id(self, reserva_id: str) -> Optional[ReservaResponse]:
        """Busca uma reserva por ID"""
        reserva = await self.reserva_repository.obter_reserva_por_id(reserva_id)
        if reserva:
            return ReservaResponse.model_validate(reserva.model_dump())
        return None

    async def listar_reservas(self) -> List[ReservaResponse]:
        """Lista todas as reservas"""
        reservas = await self.reserva_repository.listar_reservas()
        return [ReservaResponse.model_validate(reserva.model_dump()) for reserva in reservas]

    async def listar_reservas_por_cliente(self, cliente_id: str) -> List[ReservaResponse]:
        """Lista reservas de um cliente específico"""
        # Validar se cliente existe
        cliente = self.cliente_repository.obter_cliente_por_id(uuid.UUID(cliente_id))
        if not cliente:
            raise ValueError("Cliente não encontrado")
            
        reservas = await self.reserva_repository.listar_reservas_por_cliente(cliente_id)
        return [ReservaResponse.model_validate(reserva.model_dump()) for reserva in reservas]

    async def listar_reservas_por_sessao(self, sessao_id: str) -> List[ReservaResponse]:
        """Lista reservas de uma sessão específica"""
        # Validar se sessão existe
        sessao = self.sessao_repository.obter_sessao_por_id(uuid.UUID(sessao_id))
        if not sessao:
            raise ValueError("Sessão não encontrada")
            
        reservas = await self.reserva_repository.listar_reservas_por_sessao(sessao_id)
        return [ReservaResponse.model_validate(reserva.model_dump()) for reserva in reservas]

    async def atualizar_status_reserva(self, reserva_id: str, novo_status: StatusReservaEnum) -> Optional[ReservaResponse]:
        """Atualiza o status de uma reserva com validações"""
        reserva_atual = await self.reserva_repository.obter_reserva_por_id(reserva_id)
        if not reserva_atual:
            raise ValueError("Reserva não encontrada")
        
        # Validar transição de status
        if not validar_transicao_status(reserva_atual.status, novo_status):
            raise ValueError(f"Transição de status inválida: {reserva_atual.status} -> {novo_status}")
        
        reserva_data = ReservaUpdate(status=novo_status)
        reserva_atualizada = await self.reserva_repository.atualizar_reserva(reserva_id, reserva_data)
        
        if reserva_atualizada:
            return ReservaResponse.model_validate(reserva_atualizada.model_dump())
        return None

    async def cancelar_reserva(self, reserva_id: str) -> Optional[ReservaResponse]:
        """Cancela uma reserva"""
        return await self.atualizar_status_reserva(reserva_id, StatusReservaEnum.CANCELADA)

    async def confirmar_reserva(self, reserva_id: str) -> Optional[ReservaResponse]:
        """Confirma uma reserva"""
        return await self.atualizar_status_reserva(reserva_id, StatusReservaEnum.CONFIRMADA)

    async def deletar_reserva(self, reserva_id: str) -> bool:
        """Deleta uma reserva permanentemente"""
        return await self.reserva_repository.deletar_reserva(reserva_id)
