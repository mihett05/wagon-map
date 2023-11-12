from typing import Optional

import pymongo
from beanie import Document

from models.station import Station
from schemas.geojson import GeoJSON


class StationDocument(Document):
    id: int
    coordinates: GeoJSON

    class Settings:
        indexes = [[("coordinates", pymongo.GEOSPHERE)]]

    @classmethod
    async def by_id(cls, id: int) -> Optional["StationDocument"]:
        """Get a station by id."""
        return await cls.find_one(cls.id == id)

    @classmethod
    def from_model(cls, station: Station):
        return StationDocument(**{"id": station.id,
                                  "coordinates": GeoJSON.point(lat=station.lat, lon=station.lon)})

    @classmethod
    def from_values(cls, station_id: int, lat: float, lon: float):
        return StationDocument(**{"id": station_id,
                                  "coordinates": GeoJSON.point(lat=lat, lon=lon)})
