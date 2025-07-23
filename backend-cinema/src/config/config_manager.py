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

            # MQTT
            ConfigName.MQTT_BROKER_URL: os.getenv(ConfigName.MQTT_BROKER_URL, "mqtt://localhost:1883"),
            ConfigName.MQTT_BROKER_PORT: os.getenv(ConfigName.MQTT_BROKER_PORT, "1883"),
            ConfigName.MQTT_BROKER_CLIENT_ID: os.getenv(ConfigName.MQTT_BROKER_CLIENT_ID, "client_id"),

            # PostgreSQL
            ConfigName.POSTGRES_HOST: os.getenv(ConfigName.POSTGRES_HOST, "localhost"),
            ConfigName.POSTGRES_PORT: os.getenv(ConfigName.POSTGRES_PORT, "5432"),
            ConfigName.POSTGRES_DATABASE: os.getenv(ConfigName.POSTGRES_DATABASE, "cinema_db"),
            ConfigName.POSTGRES_USER: os.getenv(ConfigName.POSTGRES_USER, "postgres"),
            ConfigName.POSTGRES_PASSWORD: os.getenv(ConfigName.POSTGRES_PASSWORD, "postgres123"),
            
            # MongoDB
            ConfigName.MONGO_INITDB_ROOT_USERNAME: os.getenv(ConfigName.MONGO_INITDB_ROOT_USERNAME, "admin"),
            ConfigName.MONGO_INITDB_ROOT_PASSWORD: os.getenv(ConfigName.MONGO_INITDB_ROOT_PASSWORD, "password"),
            ConfigName.MONGO_INITDB_DATABASE: os.getenv(ConfigName.MONGO_INITDB_DATABASE, "cinema_db"),
            ConfigName.DATABASE_URL: os.getenv(ConfigName.DATABASE_URL, "mongodb://admin:password@mongo:27017/cinema_db?authSource=admin")
        }

    def get(self, key: ConfigName):
        return self._env[key]
    
    def get_database_url(self):
        host = self.get(ConfigName.POSTGRES_HOST)
        port = self.get(ConfigName.POSTGRES_PORT)
        database = self.get(ConfigName.POSTGRES_DATABASE)
        user = self.get(ConfigName.POSTGRES_USER)
        password = self.get(ConfigName.POSTGRES_PASSWORD)
        
        return f"postgresql://{user}:{password}@{host}:{port}/{database}"
    
    def get_mongodb_url(self):
        """Retorna a URL de conexão do MongoDB"""
        return self.get(ConfigName.DATABASE_URL)