from pydantic import BaseModel


class WsUserData(BaseModel):
    south_west: tuple[float, float]  # Снизу слева
    north_east: tuple[float, float]  # Справа сверху
    # Так легче фильтрацию делать
