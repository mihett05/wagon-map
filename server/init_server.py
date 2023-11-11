from datetime import datetime, UTC

import redis
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from config import config
from models.user import User, UserRole
from models.station import Station
from models.path import Path
from schemas.train import TrainDocument
from util.password import hash_password

redis_db = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT)


async def init_db():
    client = AsyncIOMotorClient(config.MONGO_URL)

    await init_beanie(
        database=client.data_wagon,
        document_models=[
            TrainDocument,
            User,
            Station,
            Path,
        ],
    )

    email = "admin@mail.ru"
    user = await User.by_email(email)
    if user is None:
        hashed = hash_password("12345678")
        await User(
            email=email,
            password=hashed,
            role=UserRole.ADMIN,
            email_confirmed_at=datetime.now(tz=UTC)
        ).create()
