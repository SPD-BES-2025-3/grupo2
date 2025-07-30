import os
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from pydantic import BaseModel
from config.database import engine, Base
from models.reserva_model import Reserva
from controllers.cliente_controller import router as cliente_router
from controllers.filme_controller import router as filme_router
from controllers.sessao_controller import router as sessao_router
from controllers.reserva_controller import router as reserva_router
from controllers.plate_event_driven_controller import PlateEventDrivenController
from config.config_manager import ConfigManager
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
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
from controllers.plate_event_driven_controller import PlateEventDrivenController
from config.config_manager import ConfigManager
from pydantic import BaseModel

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Variável global para o controller de placas
plate_controller = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gerencia o ciclo de vida da aplicação FastAPI.
    
    - STARTUP: Inicializa MongoDB, PostgreSQL e PlateEventDrivenController
    - SHUTDOWN: Finaliza graciosamente o PlateEventDrivenController
    """
    global plate_controller
    
    # === STARTUP ===
    try:
        logger.info("🚀 Iniciando aplicação Cinema Drive-in...")
        
        # 1. Inicializar PostgreSQL
        try:
            Base.metadata.create_all(bind=engine)
            logger.info("✅ PostgreSQL inicializado com sucesso!")
        except Exception as e:
            logger.warning(f"⚠️ PostgreSQL já inicializado ou erro: {e}")

        # 2. Inicializar MongoDB
        database_url = os.getenv("DATABASE_URL")
        if database_url:
            client = AsyncIOMotorClient(database_url)
            await init_beanie(database=client.cinema_db, document_models=[Reserva])
            logger.info("✅ MongoDB inicializado com sucesso!")
        else:
            logger.warning("⚠️ DATABASE_URL não configurada para MongoDB")

        # 3. Inicializar PlateEventDrivenController
        try:
            plate_controller = PlateEventDrivenController()
            await plate_controller.start()
            logger.info("✅ PlateEventDrivenController iniciado com sucesso!")
        except Exception as e:
            logger.error(f"❌ Erro ao iniciar PlateEventDrivenController: {e}")
            logger.warning("⚠️ Aplicação continuará sem processamento de placas")

        logger.info("🎬 Cinema Drive-in API totalmente operacional!")
        
    except Exception as e:
        logger.error(f"❌ Erro crítico na inicialização: {e}")
        raise

    # === YIELD CONTROL TO FASTAPI ===
    yield

    # === SHUTDOWN ===
    try:
        logger.info("🛑 Finalizando aplicação Cinema Drive-in...")
        
        # Finalizar PlateEventDrivenController graciosamente
        if plate_controller:
            await plate_controller.stop()
            logger.info("✅ PlateEventDrivenController finalizado com sucesso!")
            
        logger.info("👋 Aplicação finalizada com sucesso!")
        
    except Exception as e:
        logger.error(f"❌ Erro durante finalização: {e}")

# Criação das tabelas do PostgreSQL (executada apenas uma vez)
try:
    Base.metadata.create_all(bind=engine)
except Exception:
    # Ignora erros se as tabelas já existirem
    pass

app = FastAPI(
    title="Cinema Drive-in API",
    description="API para gerenciamento de cinema drive-in com processamento automático de placas",
    version="1.0.0",
    lifespan=lifespan  # Usar o lifespan manager
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
    """Endpoint para verificar se a API está funcionando."""
    return {
        "status": "healthy", 
        "service": "cinema-drive-in-api",
        "plate_processing": plate_controller is not None and plate_controller.is_running
    }

class PlateTestRequest(BaseModel):
    gate_id: str
    image_base64: str

@app.post("/test/plate-processing")
async def test_plate_processing(request: PlateTestRequest):
    """
    Endpoint para testar o processamento de placas diretamente.
    
    Args:
        request: Dados da requisição com gate_id e image_base64
        
    Returns:
        Resultado do processamento da placa
    """
    if not plate_controller:
        raise HTTPException(
            status_code=503, 
            detail="PlateEventDrivenController não está disponível"
        )
    
    try:
        result = await plate_controller.process_simple_image(
            gate_id=request.gate_id,
            image_base64=request.image_base64
        )
        return result
    except Exception as e:
        logger.error(f"Erro no teste de processamento de placa: {e}")
        raise HTTPException(
            status_code=500, 
            detail=f"Erro no processamento: {str(e)}"
        )

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
