import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from config.database import engine, Base
from models.reserva_model import Reserva
from controllers.cliente_controller import router as cliente_router
from controllers.filme_controller import router as filme_router
from controllers.sessao_controller import router as sessao_router
from controllers.reserva_controller import router as reserva_router
from config.config_manager import ConfigManager

try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    pass

app = FastAPI(
    title="Cinema Drive-in API",
    description="API para gerenciamento de cinema drive-in",
    version="1.0.0"
)


# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(cliente_router)
app.include_router(filme_router)
app.include_router(sessao_router)
app.include_router(reserva_router)

# Rota de teste
@app.get("/")
def read_root():
    return {"message": "Cinema Drive-in API está funcionando!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "cinema-drive-in-api"}

@app.on_event("startup")
async def startup_event():
    """Eventos executados na inicialização da aplicação"""
    # Inicializar banco PostgreSQL
    print("PostgreSQL inicializado com sucesso!")
    database_url = os.getenv("DATABASE_URL")
    client = AsyncIOMotorClient(database_url)
    await init_beanie(database=client.cinema_db, document_models=[Reserva])

if __name__ == "__main__":
    import uvicorn
    config_manager = ConfigManager()
    port = int(config_manager.get("APP_PORT"))
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True  # Apenas para desenvolvimento
    )
