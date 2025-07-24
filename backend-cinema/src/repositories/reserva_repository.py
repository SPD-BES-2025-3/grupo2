from typing import List, Optional
from models.reserva_model import Reserva, StatusReservaEnum
from schemas.reserva_schema import ReservaCreate, ReservaUpdate

class ReservaRepository:
    
    async def criar_reserva(self, reserva_data: ReservaCreate) -> Reserva:
        """Cria uma nova reserva no MongoDB"""
        reserva = Reserva(
            sessao_id=reserva_data.sessao_id,
            cliente_id=reserva_data.cliente_id,
            status=StatusReservaEnum.PENDENTE
        )
        await reserva.insert()
        return reserva

    async def obter_reserva_por_id(self, reserva_id: str) -> Optional[Reserva]:
        """Busca uma reserva por ID"""
        return await Reserva.get(reserva_id)

    async def listar_reservas(self) -> List[Reserva]:
        """Lista todas as reservas"""
        return await Reserva.find_all().to_list()

    async def listar_reservas_por_cliente(self, cliente_id: str) -> List[Reserva]:
        """Lista reservas de um cliente específico"""
        return await Reserva.find(Reserva.cliente_id == cliente_id).to_list()

    async def listar_reservas_por_sessao(self, sessao_id: str) -> List[Reserva]:
        """Lista reservas de uma sessão específica"""
        return await Reserva.find(Reserva.sessao_id == sessao_id).to_list()

    async def atualizar_reserva(self, reserva_id: str, reserva_data: ReservaUpdate) -> Optional[Reserva]:
        """Atualiza uma reserva existente"""
        reserva = await self.obter_reserva_por_id(reserva_id)
        if not reserva:
            return None
            
        update_data = reserva_data.model_dump(exclude_unset=True)
        await reserva.update({"$set": update_data})
        return await self.obter_reserva_por_id(reserva_id)

    async def deletar_reserva(self, reserva_id: str) -> bool:
        """Deleta uma reserva"""
        reserva = await self.obter_reserva_por_id(reserva_id)
        if not reserva:
            return False
        await reserva.delete()
        return True