from pydantic import BaseModel


class Station(BaseModel):
    id: int
    lat: float
    lon: float
