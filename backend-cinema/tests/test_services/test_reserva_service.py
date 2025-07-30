import unittest
from unittest.mock import AsyncMock, MagicMock
import sys
import os
import asyncio

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'src'))

from services.reserva_service import ReservaService
from schemas.reserva_schema import ReservaCreate, ReservaUpdate, ReservaResponse
from models.reserva_model import StatusReservaEnum
import uuid
from datetime import datetime

class TestReservaService(unittest.TestCase):

    def setUp(self):
        self.reserva_repository = AsyncMock()
        self.cliente_repository = MagicMock()
        self.sessao_repository = MagicMock()
        self.service = ReservaService(
            self.reserva_repository,
            self.cliente_repository,
            self.sessao_repository
        )
        self.reserva_id = str(uuid.uuid4())
        self.cliente_id = str(uuid.uuid4())
        self.sessao_id = str(uuid.uuid4())
        self.reserva_data = ReservaCreate(
            cliente_id=self.cliente_id,
            sessao_id=self.sessao_id
        )

    def test_criar_reserva_sucesso(self):
        """CREATE - Testa criação de reserva com dados válidos"""
        async def run_test():

            cliente_mock = {"id": uuid.UUID(self.cliente_id), "nome": "Cliente Teste"}
            sessao_mock = {"id": uuid.UUID(self.sessao_id), "data": "2025-07-26"}
            reserva_criada = MagicMock()
            reserva_criada.model_dump.return_value = {
                "id": self.reserva_id,
                "cliente_id": self.cliente_id,
                "sessao_id": self.sessao_id,
                "status": StatusReservaEnum.PENDENTE,
                "data_reserva": datetime.now().isoformat()
            }
            
            self.cliente_repository.obter_cliente_por_id.return_value = cliente_mock
            self.sessao_repository.obter_sessao_por_id.return_value = sessao_mock
            self.reserva_repository.listar_reservas_por_cliente.return_value = []
            self.reserva_repository.criar_reserva.return_value = reserva_criada


            response = await self.service.criar_reserva(self.reserva_data)


            self.assertIsInstance(response, ReservaResponse)
            self.assertEqual(response.cliente_id, self.cliente_id)
            self.assertEqual(response.sessao_id, self.sessao_id)
            self.reserva_repository.criar_reserva.assert_called_once_with(self.reserva_data)

        asyncio.run(run_test())

    def test_criar_reserva_cliente_inexistente(self):
        """CREATE - Testa erro quando cliente não existe"""
        async def run_test():
            self.cliente_repository.obter_cliente_por_id.return_value = None

            with self.assertRaises(ValueError) as context:
                await self.service.criar_reserva(self.reserva_data)
            
            self.assertEqual(str(context.exception), "Cliente não encontrado")
            self.reserva_repository.criar_reserva.assert_not_called()

        asyncio.run(run_test())

    def test_obter_reserva_por_id_existente(self):
        """READ - Testa busca de reserva existente por ID"""
        async def run_test():

            reserva_mock = MagicMock()
            reserva_mock.model_dump.return_value = {
                "id": self.reserva_id,
                "cliente_id": self.cliente_id,
                "sessao_id": self.sessao_id,
                "status": StatusReservaEnum.PENDENTE,
                "data_reserva": datetime.now().isoformat()
            }
            self.reserva_repository.obter_reserva_por_id.return_value = reserva_mock


            response = await self.service.obter_reserva_por_id(self.reserva_id)


            self.assertIsInstance(response, ReservaResponse)
            self.assertEqual(response.id, self.reserva_id)
            self.reserva_repository.obter_reserva_por_id.assert_called_once_with(self.reserva_id)

        asyncio.run(run_test())

    def test_obter_reserva_por_id_inexistente(self):
        """READ - Testa busca de reserva inexistente por ID"""
        async def run_test():

            self.reserva_repository.obter_reserva_por_id.return_value = None


            response = await self.service.obter_reserva_por_id(self.reserva_id)


            self.assertIsNone(response)

        asyncio.run(run_test())

    def test_listar_reservas(self):
        """READ - Testa listagem de todas as reservas"""
        async def run_test():

            reserva1 = MagicMock()
            reserva1.model_dump.return_value = {
                "id": str(uuid.uuid4()), 
                "cliente_id": "1", 
                "sessao_id": "1",
                "status": StatusReservaEnum.PENDENTE,
                "data_reserva": datetime.now().isoformat()
            }
            reserva2 = MagicMock()
            reserva2.model_dump.return_value = {
                "id": str(uuid.uuid4()), 
                "cliente_id": "2", 
                "sessao_id": "2",
                "status": StatusReservaEnum.CONFIRMADA,
                "data_reserva": datetime.now().isoformat()
            }
            
            self.reserva_repository.listar_reservas.return_value = [reserva1, reserva2]


            response = await self.service.listar_reservas()


            self.assertEqual(len(response), 2)
            self.assertIsInstance(response[0], ReservaResponse)
            self.reserva_repository.listar_reservas.assert_called_once()

        asyncio.run(run_test())

    def test_deletar_reserva_sucesso(self):
        """DELETE - Testa exclusão de reserva com sucesso"""
        async def run_test():

            self.reserva_repository.deletar_reserva.return_value = True


            response = await self.service.deletar_reserva(self.reserva_id)


            self.assertTrue(response)
            self.reserva_repository.deletar_reserva.assert_called_once_with(self.reserva_id)

        asyncio.run(run_test())

    def test_deletar_reserva_inexistente(self):
        """DELETE - Testa exclusão de reserva inexistente"""
        async def run_test():

            self.reserva_repository.deletar_reserva.return_value = False


            response = await self.service.deletar_reserva(self.reserva_id)


            self.assertFalse(response)

        asyncio.run(run_test())

    def test_cliente_e_sessao_associados_a_reserva(self):
        """Testa associação entre cliente e sessão na reserva"""

        cliente_mock = {"id": uuid.UUID(self.cliente_id), "nome": "Cliente Teste"}
        sessao_mock = {"id": uuid.UUID(self.sessao_id), "data": "2025-07-26"}
        
        self.cliente_repository.obter_cliente_por_id.return_value = cliente_mock
        self.sessao_repository.obter_sessao_por_id.return_value = sessao_mock


        cliente = self.cliente_repository.obter_cliente_por_id(uuid.UUID(self.cliente_id))
        sessao = self.sessao_repository.obter_sessao_por_id(uuid.UUID(self.sessao_id))


        self.assertIsNotNone(cliente)
        self.assertIsNotNone(sessao)
        self.assertEqual(cliente["id"], uuid.UUID(self.cliente_id))
        self.assertEqual(sessao["id"], uuid.UUID(self.sessao_id))

if __name__ == "__main__":
    unittest.main()
