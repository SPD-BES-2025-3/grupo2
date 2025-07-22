from repositories.sessao_repository import SessaoRepository
from repositories.filme_repository import FilmeRepository
from schemas.sessao_schema import SessaoCreate, SessaoUpdate, SessaoResponse
from utils.validators import validar_data_sessao, validar_hora_sessao, validar_preco_sessao
from typing import List, Optional
import uuid


class SessaoService:
    def __init__(self, sessao_repository: SessaoRepository, filme_repository: FilmeRepository):
        self.sessao_repository = sessao_repository
        self.filme_repository = filme_repository

    def criar_sessao(self, sessao_data: SessaoCreate) -> SessaoResponse:
        if not validar_data_sessao(sessao_data.data):
            raise ValueError("Data inválida")
        
        if not validar_hora_sessao(sessao_data.hora):
            raise ValueError("Hora inválida")
        
        if not validar_preco_sessao(sessao_data.preco_por_veiculo):
            raise ValueError("Preço inválido")
        
        filme = self.filme_repository.obter_filme_por_id(sessao_data.filme_id)
        if not filme:
            raise ValueError("Filme não encontrado")
        
        sessao = self.sessao_repository.criar_sessao(sessao_data)
        return SessaoResponse.model_validate(sessao)

    def obter_sessao_por_id(self, sessao_id: uuid.UUID) -> Optional[SessaoResponse]:
        sessao = self.sessao_repository.obter_sessao_por_id(sessao_id)
        if sessao:
            return SessaoResponse.model_validate(sessao)
        return None

    def obter_sessoes_por_filme(self, filme_id: uuid.UUID) -> List[SessaoResponse]:
        sessoes = self.sessao_repository.obter_sessoes_por_filme(filme_id)
        return [SessaoResponse.model_validate(sessao) for sessao in sessoes]

    def obter_todas_sessoes(self, skip: int = 0, limit: int = 100) -> List[SessaoResponse]:
        sessoes = self.sessao_repository.obter_todas_sessoes(skip, limit)
        return [SessaoResponse.model_validate(sessao) for sessao in sessoes]

    def atualizar_sessao(self, sessao_id: uuid.UUID, sessao_data: SessaoUpdate) -> Optional[SessaoResponse]:
        if sessao_data.data and not validar_data_sessao(sessao_data.data):
            raise ValueError("Data inválida")
        if sessao_data.hora and not validar_hora_sessao(sessao_data.hora):
            raise ValueError("Hora inválida")
        if sessao_data.preco_por_veiculo and not validar_preco_sessao(sessao_data.preco_por_veiculo):
            raise ValueError("Preço inválido")
        if sessao_data.filme_id:
            from utils.validators import validar_filme_id
            if not validar_filme_id(sessao_data.filme_id):
                raise ValueError("ID do filme inválido")
            filme = self.filme_repository.obter_filme_por_id(sessao_data.filme_id)
            if not filme:
                raise ValueError("Filme não encontrado")
        sessao_atualizada = self.sessao_repository.atualizar_sessao(sessao_id, sessao_data)
        if sessao_atualizada:
            return SessaoResponse.model_validate(sessao_atualizada)
        return None

    def excluir_sessao(self, sessao_id: uuid.UUID) -> bool:
        return self.sessao_repository.excluir_sessao(sessao_id)
