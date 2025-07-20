import os
from .config_name import ConfigName

class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance.__load_env()
        return cls._instance
    
    def __load_env(self):
        self._env = {
            ConfigName.APP_PORT: os.getenv(ConfigName.APP_PORT, "8000"),
            ConfigName.MONGODB_CONNECTION_STRING: os.getenv(ConfigName.MONGODB_CONNECTION_STRING, "mongodb://localhost:27017"),
            ConfigName.MONGODB_DATABASE_NAME: os.getenv(ConfigName.MONGODB_DATABASE_NAME, "cinema_db"),
            ConfigName.MONGODB_DATABASE_COLLECTION_NAME: os.getenv(ConfigName.MONGODB_DATABASE_COLLECTION_NAME, "movies")
        }

    def get(self, key: ConfigName):
        return self._env[key]