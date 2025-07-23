from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection, AsyncIOMotorDatabase
from typing import Any

from config import ConfigManager, ConfigName


class MongoDBAdapter:
    def __init__(self):
        """
        Inicializa o adaptador com a string de conexão e o nome do banco de dados.
        """
        env_config = ConfigManager()
        conn_str = env_config.get(ConfigName.MONGODB_CONNECTION_STRING)
        db_name = env_config.get(ConfigName.MONGODB_DATABASE_NAME)
        self._client = AsyncIOMotorClient(conn_str, tz_aware=True)
        self._database = self._client[db_name]

    def get_database(self) -> AsyncIOMotorDatabase[Any]:
        """
        Retorna a instância do banco de dados.
        """
        return self._database

    def get_collection(self, collection_name: str) -> AsyncIOMotorCollection:
        """
        Retorna a instância de uma coleção específica do banco de dados.
        """
        return self._database[collection_name]

    async def close(self):
        """
        Fecha a conexão com o banco de dados.
        """
        self._client.close()