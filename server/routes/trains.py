import pickle
from typing import Annotated

from fastapi import APIRouter, Depends, Response
from fastapi.responses import JSONResponse

from models.wagon import Wagon
from schemas.user import UserDocument
from routes.deps import get_user
from util.build_path import get_shortest_path

from init_server import redis_db

trains_router = APIRouter(
    prefix="/trains",
    tags=["trains"]
)


@trains_router.post("/wagon/{wagon_id}")
async def add_wagon(body: Wagon):

    pickled_wagon = pickle.dumps(body)
    redis_db.hset(name="wagon", key=body.wagon_id, value=pickled_wagon)

    return Response(status_code=200)


@trains_router.get("/wagon/{wagon_id}")
async def add_wagon(wagon_id: int):
    cache = redis_db.hget(name="wagon", key=wagon_id)

    if cache is None:
        return JSONResponse(content=f"Wagon with {wagon_id=} was not found", status_code=404)

    wagon = pickle.loads(cache)
    return JSONResponse(content=wagon.to_json(), status_code=200)


@trains_router.get("/path")
async def get_path(station_1: int, station_2: int, user: Annotated[UserDocument, Depends(get_user)]):

    return JSONResponse(content={"way": get_shortest_path(station_1, station_2)})
