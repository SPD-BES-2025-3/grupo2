from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config_manager import ConfigManager, ConfigName

config = ConfigManager()
DATABASE_URL = config.get(ConfigName.POSTGRES_CONNECTION_STRING)

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()