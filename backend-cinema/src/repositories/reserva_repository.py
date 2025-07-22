from models.reserva_model import Reserva

class ReservaRepository:
    async def criar_reserva(self, reserva_data: ReservaCreate) -> Reserva:
        reserva = Reserva(
            sessao_id=reserva_data.sessao_id,
            cliente_id=reserva_data.cliente_id,
            status=StatusReservaEnum.PENDENTE
        )
        await reserva.insert()
        return reserva

    async def obter_reserva_por_id(self, reserva_id: str) -> Reserva:
        return await Reserva.get(reserva_id)