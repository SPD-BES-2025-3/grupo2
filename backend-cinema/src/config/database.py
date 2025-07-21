from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config_manager import ConfigManager

config = ConfigManager()
DATABASE_URL = config.get_database_url()

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=True,          # Para debug - remover em produção
    pool_recycle=3600,  # Recicla conexões a cada hora
    pool_size=10,       # Tamanho do pool de conexões
    max_overflow=20     # Máximo de conexões extras
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise
    finally:
        db.close()
