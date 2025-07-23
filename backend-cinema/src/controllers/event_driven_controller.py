import asyncio
import json
import base64
from datetime import datetime
from typing import Optional

from src.models.dtos.plate_image_event import PlateImageEvent
from src.infrastructure.adapters.mqtt_broker_adapter import MQTTBrokerAdapter, MQTTConfig
from src.config import ConfigManager, ConfigName


class PlateEventDrivenController:
    """Controller para processar eventos de placas via MQTT."""
    
    def __init__(self):
        env_config = ConfigManager()
        mqtt_config = MQTTConfig(
            broker_url=env_config.get(ConfigName.MQTT_BROKER_URL),
            broker_port=int(env_config.get(ConfigName.MQTT_BROKER_PORT)),
            client_id=f"{env_config.get(ConfigName.MQTT_BROKER_CLIENT_ID)}_plates"
        )
        self.mqtt_broker = MQTTBrokerAdapter(mqtt_config)
        self.mqtt_broker.set_event_loop(asyncio.get_event_loop())
    #   self.logger = get_custom_logger(PlateEventDrivenController.__name__)
    #   self.plate_service = PlateProcessingService()