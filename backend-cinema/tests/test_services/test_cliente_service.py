import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'src'))

from services.cliente_service import ClienteService
from schemas.cliente_schema import ClienteCreate, ClienteUpdate, ClienteResponse
import uuid

class TestClienteService(unittest.TestCase):

    def setUp(self):
        self.cliente_repository = MagicMock()
        self.service = ClienteService(self.cliente_repository)
        self.cliente_id = uuid.uuid4()
        self.cliente_data = ClienteCreate(
            nome="Cliente Teste",
            email="teste@teste.com",
            placa="ABC1234"
        )

    @patch('services.cliente_service.validar_email')
    @patch('services.cliente_service.validar_placa')
    def test_criar_cliente_sucesso(self, mock_validar_placa, mock_validar_email):
        """CREATE - Testa criação de cliente com dados válidos"""
        mock_validar_email.return_value = True
        mock_validar_placa.return_value = True
        self.cliente_repository.obter_cliente_por_email.return_value = None
        self.cliente_repository.criar_cliente.return_value = {
            "id": self.cliente_id,
            "nome": self.cliente_data.nome,
            "email": self.cliente_data.email,
            "placa": self.cliente_data.placa
        }

        response = self.service.criar_cliente(self.cliente_data)

        self.assertIsInstance(response, ClienteResponse)
        self.assertEqual(response.id, self.cliente_id)
        self.assertEqual(response.email, self.cliente_data.email)
        self.assertEqual(response.placa, self.cliente_data.placa)
        self.cliente_repository.criar_cliente.assert_called_once_with(self.cliente_data)

    @patch('services.cliente_service.validar_email')
    def test_criar_cliente_email_invalido(self, mock_validar_email):
        """CREATE - Testa erro quando email é inválido"""
        mock_validar_email.return_value = False

        with self.assertRaises(ValueError) as context:
            self.service.criar_cliente(self.cliente_data)
        
        self.assertEqual(str(context.exception), "Email inválido")
        self.cliente_repository.criar_cliente.assert_not_called()

    @patch('services.cliente_service.validar_email')
    @patch('services.cliente_service.validar_placa')
    def test_criar_cliente_email_ja_existe(self, mock_validar_placa, mock_validar_email):
        """CREATE - Testa erro quando email já está em uso"""
        mock_validar_email.return_value = True
        mock_validar_placa.return_value = True
        self.cliente_repository.obter_cliente_por_email.return_value = {"id": uuid.uuid4()}

        with self.assertRaises(ValueError) as context:
            self.service.criar_cliente(self.cliente_data)
        
        self.assertEqual(str(context.exception), "Email já está em uso")
        self.cliente_repository.criar_cliente.assert_not_called()

    def test_obter_cliente_por_id_existente(self):
        """READ - Testa busca de cliente existente por ID"""
        cliente_mock = {
            "id": self.cliente_id,
            "nome": "Cliente Teste",
            "email": "teste@teste.com",
            "placa": "ABC1234"
        }
        self.cliente_repository.obter_cliente_por_id.return_value = cliente_mock

        response = self.service.obter_cliente_por_id(self.cliente_id)

        self.assertIsInstance(response, ClienteResponse)
        self.assertEqual(response.id, self.cliente_id)
        self.cliente_repository.obter_cliente_por_id.assert_called_once_with(self.cliente_id)

    def test_obter_cliente_por_id_inexistente(self):
        """READ - Testa busca de cliente inexistente por ID"""
        self.cliente_repository.obter_cliente_por_id.return_value = None

        response = self.service.obter_cliente_por_id(self.cliente_id)

        self.assertIsNone(response)

    def test_obter_todos_clientes(self):
        """READ - Testa listagem de todos os clientes"""
        clientes_mock = [
            {"id": uuid.uuid4(), "nome": "Cliente 1", "email": "cliente1@teste.com", "placa": "ABC1234"},
            {"id": uuid.uuid4(), "nome": "Cliente 2", "email": "cliente2@teste.com", "placa": "DEF5678"}
        ]
        self.cliente_repository.obter_todos_clientes.return_value = clientes_mock

        response = self.service.obter_todos_clientes(skip=0, limit=10)

        self.assertEqual(len(response), 2)
        self.assertIsInstance(response[0], ClienteResponse)
        self.cliente_repository.obter_todos_clientes.assert_called_once_with(0, 10)

    @patch('services.cliente_service.validar_email')
    def test_atualizar_cliente_sucesso(self, mock_validar_email):
        """UPDATE - Testa atualização de cliente com sucesso"""
        update_data = ClienteUpdate(nome="Nome Atualizado", email="novo@teste.com")
        mock_validar_email.return_value = True
        self.cliente_repository.obter_cliente_por_email.return_value = None
        cliente_atualizado = {
            "id": self.cliente_id,
            "nome": "Nome Atualizado",
            "email": "novo@teste.com",
            "placa": "ABC1234"
        }
        self.cliente_repository.atualizar_cliente.return_value = cliente_atualizado

        response = self.service.atualizar_cliente(self.cliente_id, update_data)

        self.assertIsInstance(response, ClienteResponse)
        self.assertEqual(response.nome, "Nome Atualizado")
        self.cliente_repository.atualizar_cliente.assert_called_once_with(self.cliente_id, update_data)

    def test_atualizar_cliente_inexistente(self):
        """UPDATE - Testa atualização de cliente inexistente"""
        update_data = ClienteUpdate(nome="Nome Atualizado")
        self.cliente_repository.atualizar_cliente.return_value = None

        response = self.service.atualizar_cliente(self.cliente_id, update_data)

        self.assertIsNone(response)

    def test_deletar_cliente_sucesso(self):
        """DELETE - Testa exclusão de cliente com sucesso"""
        self.cliente_repository.deletar_cliente.return_value = True

        response = self.service.deletar_cliente(self.cliente_id)

        self.assertTrue(response)
        self.cliente_repository.deletar_cliente.assert_called_once_with(self.cliente_id)

    def test_deletar_cliente_inexistente(self):
        """DELETE - Testa exclusão de cliente inexistente"""
        self.cliente_repository.deletar_cliente.return_value = False

        response = self.service.deletar_cliente(self.cliente_id)

        self.assertFalse(response)

if __name__ == "__main__":
    unittest.main()
