from motor.motor_asyncio import AsyncIOMotorClient
from config_manager import ConfigManager, ConfigName

config = ConfigManager()
MONGO_URL = config.get(ConfigName.MONGODB_CONNECTION_STRING)
MONGO_DB = config.get(ConfigName.MONGODB_DATABASE_NAME)

client = AsyncIOMotorClient(MONGO_URL)
mongo_db = client[MONGO_DB]