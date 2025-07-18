from config import ConfigManager, ConfigName

import logging
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from controllers. import
# from config.database import DatabaseManager

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Cinema Drive-in API",
    description="API for managing cinema operations",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Cinema On-drive API",
        "version": "1.0.0",
        "status": "Running"
    }

if __name__ == "__main__":

    config_manager = ConfigManager()
    server_port = config_manager.get(ConfigName.APP_PORT)
    
    uvicorn.run(
        "main:app",
        host="localhost",
        port=int(server_port),
        reload=True,
        log_level="debug",
        use_colors=True,
    )