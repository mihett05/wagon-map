from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field


class EventType(str, Enum):
    UPDATE_BOUNDS = "UPDATE_BOUNDS"


class Request(BaseModel):
    uid: UUID
    event: EventType


class Response(BaseModel):
    uid: UUID = Field(default_factory=UUID)
    event: EventType = Field(default="")


class WsUserData(BaseModel):
    south_west: tuple[float, float] = Field(
        default_factory=lambda: (0, 0)
    )  # Снизу слева
    north_east: tuple[float, float] = Field(
        default_factory=lambda: (0, 0)
    )  # Справа сверху
