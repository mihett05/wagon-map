import csv
import logging
import os
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

    if config.INIT_DB_VALUES:
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

        with open(f"{os.path.dirname(os.path.realpath(__file__))}/static_data/station_coords.csv") as csvfile:
            logging.info("Start adding station coords")
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                try:
                    station_id = int(row[0])
                    station_lat = float(row[1])
                    station_lon = float(row[2])

                    document = await StationDocument.by_id(station_id)

                    if document is None:
                        await StationDocument.from_values(station_id, station_lat, station_lon).create()

                except ValueError:
                    continue
            logging.info("Finish adding station coords")
