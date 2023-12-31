from typing import Optional

import pymongo
from beanie import Document

from models.train import Train
from schemas.geojson import GeoJSON


class TrainDocument(Document):
    id: int
    coordinates: GeoJSON

    class Settings:
        indexes = [[("coordinates", pymongo.GEOSPHERE)]]

    @classmethod
    async def by_id(cls, id: int) -> Optional["TrainDocument"]:
        """Get a station by id."""
        return await cls.find_one(cls.id == id)

    @classmethod
    def from_model(cls, station: Train):
        return TrainDocument(**{"id": station.id,
                                "coordinates": GeoJSON.point(lat=station.lat, lon=station.lon)})
