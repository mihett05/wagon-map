from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from schemas.user import UserDocument
from routes.deps import get_user, get_station

trains_router = APIRouter(
    prefix="/trains",
    tags=["trains"]
)


@trains_router.get("/path")
async def get_path(station_1: int, station_2: int, user: Annotated[UserDocument, Depends(get_user)]):

    station_1, station_2 = await get_station(station_1), get_station(station_2)

    return JSONResponse(content={"station1": station_1, "station_2": station_2, "user_role": user.role})
