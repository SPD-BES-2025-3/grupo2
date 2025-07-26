import sys
import os
import unittest
from unittest.mock import MagicMock, patch

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'src'))

from services.filme_service import FilmeService
from schemas.filme_schema import FilmeCreate, FilmeUpdate, FilmeResponse
import uuid

class TestFilmeService(unittest.TestCase):

    def setUp(self):
        self.filme_repository = MagicMock()
        self.service = FilmeService(self.filme_repository)
        self.filme_id = uuid.uuid4()
        self.filme_data = FilmeCreate(
            titulo="Filme Teste",
            diretor="Diretor Teste",
            duracao_minutos=120,
            classificacao_indicativa="12",
            generos=["Ação", "Drama"]
        )

    @patch('services.filme_service.validar_titulo_filme')
    @patch('services.filme_service.validar_diretor_filme')
    @patch('services.filme_service.validar_generos_filme')
    @patch('services.filme_service.validar_duracao_filme')
    @patch('services.filme_service.validar_classificacao_indicativa')
    def test_criar_filme_sucesso(self, mock_classificacao, mock_duracao, mock_generos, mock_diretor, mock_titulo):
        """CREATE - Testa criação de filme com dados válidos"""

        mock_titulo.return_value = True
        mock_diretor.return_value = True
        mock_generos.return_value = (True, "")
        mock_duracao.return_value = True
        mock_classificacao.return_value = True
        
        self.filme_repository.criar_filme.return_value = {
            "id": self.filme_id,
            "titulo": self.filme_data.titulo,
            "diretor": self.filme_data.diretor,
            "duracao_minutos": self.filme_data.duracao_minutos,
            "classificacao_indicativa": self.filme_data.classificacao_indicativa,
            "generos": self.filme_data.generos
        }


        response = self.service.criar_filme(self.filme_data)


        self.assertIsInstance(response, FilmeResponse)
        self.assertEqual(response.id, self.filme_id)
        self.assertEqual(response.titulo, self.filme_data.titulo)
        self.assertEqual(response.diretor, self.filme_data.diretor)
        self.filme_repository.criar_filme.assert_called_once_with(self.filme_data)

    @patch('services.filme_service.validar_titulo_filme')
    def test_criar_filme_titulo_invalido(self, mock_titulo):
        """CREATE - Testa erro quando título é inválido"""
        mock_titulo.return_value = False

        with self.assertRaises(ValueError) as context:
            self.service.criar_filme(self.filme_data)
        
        self.assertEqual(str(context.exception), "Título inválido")
        self.filme_repository.criar_filme.assert_not_called()

    def test_obter_filme_por_id_existente(self):
        """READ - Testa busca de filme existente por ID"""

        filme_mock = {
            "id": self.filme_id,
            "titulo": "Filme Teste",
            "diretor": "Diretor Teste",
            "duracao_minutos": 120,
            "classificacao_indicativa": "12",
            "generos": ["Ação", "Drama"]
        }
        self.filme_repository.obter_filme_por_id.return_value = filme_mock


        response = self.service.obter_filme_por_id(self.filme_id)


        self.assertIsInstance(response, FilmeResponse)
        self.assertEqual(response.id, self.filme_id)
        self.filme_repository.obter_filme_por_id.assert_called_once_with(self.filme_id)

    def test_obter_filme_por_id_inexistente(self):
        """READ - Testa busca de filme inexistente por ID"""

        self.filme_repository.obter_filme_por_id.return_value = None


        response = self.service.obter_filme_por_id(self.filme_id)


        self.assertIsNone(response)

    def test_obter_todos_filmes(self):
        """READ - Testa listagem de todos os filmes"""

        filmes_mock = [
            {"id": uuid.uuid4(), "titulo": "Filme 1", "diretor": "Diretor 1", "duracao_minutos": 120, "classificacao_indicativa": "12", "generos": ["Ação"]},
            {"id": uuid.uuid4(), "titulo": "Filme 2", "diretor": "Diretor 2", "duracao_minutos": 90, "classificacao_indicativa": "10", "generos": ["Drama"]}
        ]
        self.filme_repository.obter_todos_filmes.return_value = filmes_mock


        response = self.service.obter_todos_filmes(skip=0, limit=10)


        self.assertEqual(len(response), 2)
        self.assertIsInstance(response[0], FilmeResponse)
        self.filme_repository.obter_todos_filmes.assert_called_once_with(0, 10)

    @patch('services.filme_service.validar_titulo_filme')
    def test_atualizar_filme_sucesso(self, mock_titulo):
        """UPDATE - Testa atualização de filme com sucesso"""

        update_data = FilmeUpdate(titulo="Título Atualizado")
        mock_titulo.return_value = True
        filme_atualizado = {
            "id": self.filme_id,
            "titulo": "Título Atualizado",
            "diretor": "Diretor Teste",
            "duracao_minutos": 120,
            "classificacao_indicativa": "12",
            "generos": ["Ação", "Drama"]
        }
        self.filme_repository.atualizar_filme.return_value = filme_atualizado


        response = self.service.atualizar_filme(self.filme_id, update_data)


        self.assertIsInstance(response, FilmeResponse)
        self.assertEqual(response.titulo, "Título Atualizado")
        self.filme_repository.atualizar_filme.assert_called_once_with(self.filme_id, update_data)

    def test_atualizar_filme_inexistente(self):
        """UPDATE - Testa atualização de filme inexistente"""

        update_data = FilmeUpdate(titulo="Título Atualizado")
        self.filme_repository.atualizar_filme.return_value = None


        response = self.service.atualizar_filme(self.filme_id, update_data)


        self.assertIsNone(response)

    def test_deletar_filme_sucesso(self):
        """DELETE - Testa exclusão de filme com sucesso"""

        self.filme_repository.deletar_filme.return_value = True


        response = self.service.deletar_filme(self.filme_id)


        self.assertTrue(response)
        self.filme_repository.deletar_filme.assert_called_once_with(self.filme_id)

    def test_deletar_filme_inexistente(self):
        """DELETE - Testa exclusão de filme inexistente"""

        self.filme_repository.deletar_filme.return_value = False


        response = self.service.deletar_filme(self.filme_id)


        self.assertFalse(response)

if __name__ == "__main__":
    unittest.main()
