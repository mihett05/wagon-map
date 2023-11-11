from pydantic import BaseModel


class GeoJSON(BaseModel):
    type: str
    coordinates: list[float]

    @classmethod
    def point(cls, lat: float, lon: float):
        return GeoJSON(type="Point", coordinates=[lon, lat])
