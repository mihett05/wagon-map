from datetime import datetime, UTC

import redis
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from config import config
from models.user import UserRole
from schemas.user import UserDocument
from schemas.station import StationDocument
from schemas.path import PathDocument
from schemas.train import TrainDocument
from util.password import hash_password

redis_db = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT)


async def init_db():
    client = AsyncIOMotorClient(config.MONGO_URL)

    await init_beanie(
        database=client.data_wagon,
        document_models=[
            TrainDocument,
            UserDocument,
            StationDocument,
            PathDocument,
        ],
    )

    email = "admin@mail.ru"
    user = await UserDocument.by_email(email)
    if user is None:
        hashed = hash_password("12345678")
        await UserDocument(
            email=email,
            password=hashed,
            role=UserRole.ADMIN,
            email_confirmed_at=datetime.now(tz=UTC)
        ).create()
