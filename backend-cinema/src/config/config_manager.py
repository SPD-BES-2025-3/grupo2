import os
from dotenv import load_dotenv
from .config_name import ConfigName

class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance.__load_env()
        return cls._instance
    
    def __load_env(self):
        # Carregar variáveis do arquivo .env
        load_dotenv()
        
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
            ConfigName.MONGODB_CONNECTION_STRING: os.getenv(ConfigName.MONGODB_CONNECTION_STRING, "mongodb://localhost:27017"),
            ConfigName.MONGODB_DATABASE_NAME: os.getenv(ConfigName.MONGODB_DATABASE_NAME, "cinema_db"),
            ConfigName.MONGODB_DATABASE_COLLECTION_NAME: os.getenv(ConfigName.MONGODB_DATABASE_COLLECTION_NAME, "reservations"),
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