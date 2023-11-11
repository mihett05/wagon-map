from pydantic import BaseModel


class Train(BaseModel):
    id: int
    lat: float
    lon: float
    # ... остальные поля поезда
