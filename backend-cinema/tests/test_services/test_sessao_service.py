import sys
import os
import unittest
from unittest.mock import MagicMock, patch

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'src'))

from services.sessao_service import SessaoService
from schemas.sessao_schema import SessaoCreate, SessaoUpdate, SessaoResponse
import uuid

class TestSessaoService(unittest.TestCase):

    def setUp(self):
        self.sessao_repository = MagicMock()
        self.filme_repository = MagicMock()
        self.service = SessaoService(self.sessao_repository, self.filme_repository)
        self.filme_id = uuid.UUID("123e4567-e89b-12d3-a456-426614174000")
        self.sessao_id = uuid.uuid4()
        self.sessao_data = SessaoCreate(
            data="2025-07-26",
            hora="20:00",
            preco_por_veiculo=50.0,
            filme_id=self.filme_id
        )

    @patch('services.sessao_service.validar_data_sessao')
    @patch('services.sessao_service.validar_hora_sessao')
    @patch('services.sessao_service.validar_preco_sessao')
    def test_criar_sessao_sucesso(self, mock_preco, mock_hora, mock_data):
        """CREATE - Testa criação de sessão com dados válidos"""

        mock_data.return_value = True
        mock_hora.return_value = True
        mock_preco.return_value = True
        self.filme_repository.obter_filme_por_id.return_value = True
        self.sessao_repository.criar_sessao.return_value = {
            "id": self.sessao_id,
            "filme_id": self.sessao_data.filme_id,
            "data": self.sessao_data.data,
            "hora": self.sessao_data.hora,
            "preco_por_veiculo": self.sessao_data.preco_por_veiculo
        }


        response = self.service.criar_sessao(self.sessao_data)


        self.assertIsInstance(response, SessaoResponse)
        self.assertEqual(response.id, self.sessao_id)
        self.assertEqual(response.data, self.sessao_data.data)
        self.sessao_repository.criar_sessao.assert_called_once_with(self.sessao_data)

    def test_criar_sessao_filme_inexistente(self):
        """CREATE - Testa erro quando filme não existe"""
        with patch('services.sessao_service.validar_data_sessao', return_value=True), \
             patch('services.sessao_service.validar_hora_sessao', return_value=True), \
             patch('services.sessao_service.validar_preco_sessao', return_value=True):
            self.filme_repository.obter_filme_por_id.return_value = None

            with self.assertRaises(ValueError) as context:
                self.service.criar_sessao(self.sessao_data)
            
            self.assertEqual(str(context.exception), "Filme não encontrado")
            self.sessao_repository.criar_sessao.assert_not_called()

    def test_criar_sessao_dados_invalidos(self):
        """CREATE - Testa comportamento com dados inválidos"""
        # Teste com preço negativo
        with self.assertRaises(ValueError):
            SessaoCreate(
                data="2025-07-26",
                hora="20:00",
                preco_por_veiculo=-10.0,  # Preço inválido
                filme_id=self.filme_id
            )

    def test_obter_sessao_por_id_existente(self):
        """READ - Testa busca de sessão existente por ID"""

        sessao_mock = {
            "id": self.sessao_id,
            "filme_id": self.filme_id,
            "data": "2025-07-26",
            "hora": "20:00",
            "preco_por_veiculo": 50.0
        }
        self.sessao_repository.obter_sessao_por_id.return_value = sessao_mock


        response = self.service.obter_sessao_por_id(self.sessao_id)


        self.assertIsInstance(response, SessaoResponse)
        self.assertEqual(response.id, self.sessao_id)
        self.sessao_repository.obter_sessao_por_id.assert_called_once_with(self.sessao_id)

    def test_obter_sessao_por_id_inexistente(self):
        """READ - Testa busca de sessão inexistente por ID"""

        self.sessao_repository.obter_sessao_por_id.return_value = None


        response = self.service.obter_sessao_por_id(self.sessao_id)


        self.assertIsNone(response)

    def test_obter_todas_sessoes(self):
        """READ - Testa listagem de todas as sessões"""

        sessoes_mock = [
            {"id": uuid.uuid4(), "filme_id": self.filme_id, "data": "2025-07-26", "hora": "18:00", "preco_por_veiculo": 40.0},
            {"id": uuid.uuid4(), "filme_id": self.filme_id, "data": "2025-07-26", "hora": "20:00", "preco_por_veiculo": 50.0}
        ]
        self.sessao_repository.obter_todas_sessoes.return_value = sessoes_mock


        response = self.service.obter_todas_sessoes(skip=0, limit=10)


        self.assertEqual(len(response), 2)
        self.assertIsInstance(response[0], SessaoResponse)
        self.sessao_repository.obter_todas_sessoes.assert_called_once_with(0, 10)

    def test_obter_sessoes_por_filme(self):
        """READ - Testa busca de sessões por filme"""

        sessoes_mock = [
            {"id": uuid.uuid4(), "filme_id": self.filme_id, "data": "2025-07-26", "hora": "18:00", "preco_por_veiculo": 40.0},
            {"id": uuid.uuid4(), "filme_id": self.filme_id, "data": "2025-07-27", "hora": "20:00", "preco_por_veiculo": 50.0}
        ]
        self.sessao_repository.obter_sessoes_por_filme.return_value = sessoes_mock


        response = self.service.obter_sessoes_por_filme(self.filme_id)


        self.assertEqual(len(response), 2)
        self.assertIsInstance(response[0], SessaoResponse)
        self.sessao_repository.obter_sessoes_por_filme.assert_called_once_with(self.filme_id)

    def test_atualizar_sessao_sucesso(self):
        """UPDATE - Testa atualização de sessão com sucesso"""

        update_data = SessaoUpdate(preco_por_veiculo=60.0)
        with patch('services.sessao_service.validar_preco_sessao', return_value=True):
            sessao_atualizada = {
                "id": self.sessao_id,
                "filme_id": self.filme_id,
                "data": "2025-07-26",
                "hora": "20:00",
                "preco_por_veiculo": 60.0
            }
            self.sessao_repository.atualizar_sessao.return_value = sessao_atualizada


            response = self.service.atualizar_sessao(self.sessao_id, update_data)


            self.assertIsInstance(response, SessaoResponse)
            self.assertEqual(response.preco_por_veiculo, 60.0)
            self.sessao_repository.atualizar_sessao.assert_called_once_with(self.sessao_id, update_data)

    def test_atualizar_sessao_inexistente(self):
        """UPDATE - Testa atualização de sessão inexistente"""

        update_data = SessaoUpdate(preco_por_veiculo=60.0)
        with patch('services.sessao_service.validar_preco_sessao', return_value=True):
            self.sessao_repository.atualizar_sessao.return_value = None


            response = self.service.atualizar_sessao(self.sessao_id, update_data)


            self.assertIsNone(response)

    def test_excluir_sessao_sucesso(self):
        """DELETE - Testa exclusão de sessão com sucesso"""

        self.sessao_repository.excluir_sessao.return_value = True


        response = self.service.excluir_sessao(self.sessao_id)


        self.assertTrue(response)
        self.sessao_repository.excluir_sessao.assert_called_once_with(self.sessao_id)

    def test_excluir_sessao_inexistente(self):
        """DELETE - Testa exclusão de sessão inexistente"""

        self.sessao_repository.excluir_sessao.return_value = False


        response = self.service.excluir_sessao(self.sessao_id)


        self.assertFalse(response)

if __name__ == "__main__":
    unittest.main()
