import pymongo
from beanie import Document

from schemas.geojson import GeoJSON


class Station(Document):
    id: int
    cooridnates: GeoJSON

    class Settings:
        indexes = [[("coordinates", pymongo.GEOSPHERE)]]
