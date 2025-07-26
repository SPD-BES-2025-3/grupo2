import sys
import os
import unittest
from unittest.mock import MagicMock

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'src'))

from services.sessao_service import SessaoService
from schemas.sessao_schema import SessaoCreate
import uuid

class TestSessaoService(unittest.TestCase):

    def setUp(self):
        self.sessao_repository = MagicMock()
        self.filme_repository = MagicMock()
        self.service = SessaoService(self.sessao_repository, self.filme_repository)

    def test_criar_sessao_sucesso(self):
        filme_id = uuid.UUID("123e4567-e89b-12d3-a456-426614174000")
        sessao_data = SessaoCreate(
            data="2025-07-26",
            hora="20:00",
            preco_por_veiculo=50.0,
            filme_id=filme_id
        )
        sessao_id = uuid.uuid4()
        self.filme_repository.obter_filme_por_id.return_value = True
        self.sessao_repository.criar_sessao.return_value = {
            "id": sessao_id,
            "filme_id": sessao_data.filme_id,
            "data": sessao_data.data,
            "hora": sessao_data.hora,
            "preco_por_veiculo": sessao_data.preco_por_veiculo
        }

        response = self.service.criar_sessao(sessao_data)

        self.assertEqual(response.id, sessao_id)
        self.assertEqual(response.data, sessao_data.data)
        self.assertEqual(response.hora, sessao_data.hora)
        self.assertEqual(response.preco_por_veiculo, sessao_data.preco_por_veiculo)

    def test_filme_id_associado_a_filme(self):
        filme_id = uuid.UUID("123e4567-e89b-12d3-a456-426614174000")
        self.filme_repository.obter_filme_por_id.return_value = {
            "id": filme_id,
            "titulo": "Filme Teste",
            "diretor": "Diretor Teste",
            "generos": ["Ação", "Drama"],
            "duracao_minutos": 120,
            "classificacao_indicativa": "12"
        }

        filme = self.filme_repository.obter_filme_por_id(filme_id)

        self.assertIsNotNone(filme)
        self.assertEqual(filme["id"], filme_id)
        self.assertEqual(filme["titulo"], "Filme Teste")

    def test_criar_sessao_filme_inexistente(self):
        """Testa se lança exceção quando filme não existe"""
        filme_id = uuid.UUID("123e4567-e89b-12d3-a456-426614174000")
        sessao_data = SessaoCreate(
            data="2025-07-26",
            hora="20:00",
            preco_por_veiculo=50.0,
            filme_id=filme_id
        )
        # Mock retorna None (filme não encontrado)
        self.filme_repository.obter_filme_por_id.return_value = None

        with self.assertRaises(ValueError) as context:
            self.service.criar_sessao(sessao_data)
        
        self.assertIn("Filme não encontrado", str(context.exception))

    def test_criar_sessao_verifica_chamadas_repository(self):
        """Testa se os métodos do repository são chamados corretamente"""
        filme_id = uuid.UUID("123e4567-e89b-12d3-a456-426614174000")
        sessao_data = SessaoCreate(
            data="2025-07-26",
            hora="20:00",
            preco_por_veiculo=50.0,
            filme_id=filme_id
        )
        sessao_id = uuid.uuid4()
        
        self.filme_repository.obter_filme_por_id.return_value = True
        self.sessao_repository.criar_sessao.return_value = {
            "id": sessao_id,
            "filme_id": sessao_data.filme_id,
            "data": sessao_data.data,
            "hora": sessao_data.hora,
            "preco_por_veiculo": sessao_data.preco_por_veiculo
        }

        self.service.criar_sessao(sessao_data)

        # Verifica se os métodos foram chamados com os parâmetros corretos
        self.filme_repository.obter_filme_por_id.assert_called_once_with(filme_id)
        self.sessao_repository.criar_sessao.assert_called_once_with(sessao_data)

    def test_criar_sessao_dados_invalidos(self):
        """Testa comportamento com dados inválidos"""
        filme_id = uuid.UUID("123e4567-e89b-12d3-a456-426614174000")
        
        # Teste com preço negativo
        with self.assertRaises(ValueError):
            SessaoCreate(
                data="2025-07-26",
                hora="20:00",
                preco_por_veiculo=-10.0,  # Preço inválido
                filme_id=filme_id
            )

if __name__ == "__main__":
    unittest.main()
