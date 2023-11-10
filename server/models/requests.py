from enum import Enum
from uuid import UUID

from pydantic import BaseModel

from models.train import Train


class RequestType(str, Enum):
    UPDATE_BOUNDS = "UPDATE_BOUNDS"


class Request(BaseModel):
    uid: UUID
    request_type: RequestType


class UpdateBoundsRequest(Request):
    request_type: RequestType = RequestType.UPDATE_BOUNDS
    south_west: tuple[float, float]
    north_east: tuple[float, float]


class Response(BaseModel):
    uid: UUID
    event: RequestType


class UpdateBoundsResponse(Response):
    request_type: RequestType = RequestType.UPDATE_BOUNDS
    trains: list[Train]
