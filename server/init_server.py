import redis
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from config import config
from models.user import User
from schemas.train import TrainDocument

redis_db = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT)


async def init_db():
    client = AsyncIOMotorClient(config.MONGO_URL)

    await init_beanie(database=client.data_wagon, document_models=[TrainDocument, User])
