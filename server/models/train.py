from pydantic import BaseModel


class Train(BaseModel):
    id: int
    coordinates: tuple[float, float]
    # ... остальные поля поезда