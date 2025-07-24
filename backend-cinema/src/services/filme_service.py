from repositories.filme_repository import FilmeRepository
from schemas.filme_schema import FilmeCreate, FilmeUpdate, FilmeResponse
from utils.validators import (
    validar_titulo_filme, validar_diretor_filme, validar_duracao_filme, 
    validar_classificacao_indicativa, validar_generos_filme
)
from typing import List, Optional
import uuid

class FilmeService:
    def __init__(self, filme_repository: FilmeRepository):
        self.filme_repository = filme_repository

    def criar_filme(self, filme_data: FilmeCreate) -> FilmeResponse:
        if not validar_titulo_filme(filme_data.titulo):
            raise ValueError("Título inválido")
        
        if not validar_diretor_filme(filme_data.diretor):
            raise ValueError("Diretor inválido")
        
        ok, msg = validar_generos_filme(filme_data.generos)

        if not ok:
            raise ValueError(f"Gêneros inválidos: {msg}")
        
        if not validar_duracao_filme(filme_data.duracao_minutos):
            raise ValueError("Duração inválida")
        
        if not validar_classificacao_indicativa(filme_data.classificacao_indicativa):
            raise ValueError("Classificação indicativa inválida")
        
        filme = self.filme_repository.criar_filme(filme_data)
        return FilmeResponse.model_validate(filme)

    def obter_filme_por_id(self, filme_id: uuid.UUID) -> Optional[FilmeResponse]:
        filme = self.filme_repository.obter_filme_por_id(filme_id)
        if filme:
            return FilmeResponse.model_validate(filme)
        return None

    def obter_filme_por_titulo(self, titulo: str) -> List[FilmeResponse]:
        filmes = self.filme_repository.obter_filme_por_titulo(titulo)
        return [FilmeResponse.model_validate(filme) for filme in filmes]

    def obter_todos_filmes(self, skip: int = 0, limit: int = 100) -> List[FilmeResponse]:
        filmes = self.filme_repository.obter_todos_filmes(skip, limit)
        return [FilmeResponse.model_validate(filme) for filme in filmes]

    def atualizar_filme(self, filme_id: uuid.UUID, filme_data: FilmeUpdate) -> Optional[FilmeResponse]:
        if filme_data.titulo and not validar_titulo_filme(filme_data.titulo):
            raise ValueError("Título inválido")
        if filme_data.diretor and not validar_diretor_filme(filme_data.diretor):
            raise ValueError("Diretor inválido")
        if filme_data.generos is not None:
            ok, msg = validar_generos_filme(filme_data.generos)
            if not ok:
                raise ValueError(f"Gêneros inválidos: {msg}")
        if filme_data.duracao_minutos and not validar_duracao_filme(filme_data.duracao_minutos):
            raise ValueError("Duração inválida")
        if filme_data.classificacao_indicativa and not validar_classificacao_indicativa(filme_data.classificacao_indicativa):
            raise ValueError("Classificação indicativa inválida")
        filme_atualizado = self.filme_repository.atualizar_filme(filme_id, filme_data)
        if filme_atualizado:
            return FilmeResponse.model_validate(filme_atualizado)
        return None

    def obter_generos_filme(self, filme_id: uuid.UUID) -> list:
        return self.filme_repository.obter_generos_filme(filme_id)

    def deletar_filme(self, filme_id: uuid.UUID) -> bool:
        return self.filme_repository.deletar_filme(filme_id)
