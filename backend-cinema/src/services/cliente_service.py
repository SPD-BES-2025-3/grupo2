from repositories.cliente_repository import ClienteRepository
from schemas.cliente_schema import ClienteCreate, ClienteUpdate, ClienteResponse
from utils.validators import validar_email, validar_placa
from typing import List, Optional
import uuid

class ClienteService:
    
    def __init__(self, cliente_repository: ClienteRepository):
        self.cliente_repository = cliente_repository
    
    def criar_cliente(self, cliente_data: ClienteCreate) -> ClienteResponse:
        
        if not validar_email(cliente_data.email):
            raise ValueError("Email inválido")
        
        if not validar_placa(cliente_data.placa):
            raise ValueError("Placa inválida")
        
        if self.cliente_repository.obter_cliente_por_email(cliente_data.email):
            raise ValueError("Email já está em uso")
        
        cliente = self.cliente_repository.criar_cliente(cliente_data)
        
        response = ClienteResponse.model_validate(cliente)
        
        return response
    
    def obter_cliente_por_id(self, cliente_id: uuid.UUID) -> Optional[ClienteResponse]:
        cliente = self.cliente_repository.obter_cliente_por_id(cliente_id)
        if cliente:
            return ClienteResponse.model_validate(cliente)
        return None
    
    def obter_todos_clientes(self, skip: int = 0, limit: int = 100) -> List[ClienteResponse]:
        clientes = self.cliente_repository.obter_todos_clientes(skip, limit)
        return [ClienteResponse.model_validate(cliente) for cliente in clientes]
    
    def atualizar_cliente(self, cliente_id: uuid.UUID, cliente_data: ClienteUpdate) -> Optional[ClienteResponse]:
        if cliente_data.email and not validar_email(cliente_data.email):
            raise ValueError("Email inválido")
        
        if cliente_data.placa and not validar_placa(cliente_data.placa):
            raise ValueError("Placa inválida")
        
        if cliente_data.email:
            cliente_existente = self.cliente_repository.obter_cliente_por_email(cliente_data.email)
            if cliente_existente and cliente_existente.id != cliente_id:
                raise ValueError("Email já está em uso")
        
        cliente = self.cliente_repository.atualizar_cliente(cliente_id, cliente_data)
        if cliente:
            return ClienteResponse.model_validate(cliente)
        return None
    
    def deletar_cliente(self, cliente_id: uuid.UUID) -> bool:
        return self.cliente_repository.deletar_cliente(cliente_id)
