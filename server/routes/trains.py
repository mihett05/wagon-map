from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from schemas.user import UserDocument
from routes.deps import get_user, get_station
from util.build_path import get_shortest_path

trains_router = APIRouter(
    prefix="/trains",
    tags=["trains"]
)


@trains_router.get("/path")
async def get_path(station_1: int, station_2: int, user: Annotated[UserDocument, Depends(get_user)]):

    station_1, station_2 = await get_station(station_1), await get_station(station_2)

    return JSONResponse(content={"way": get_shortest_path(station_1.id, station_2.id)})
