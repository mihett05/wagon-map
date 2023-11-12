from datetime import datetime
import json
import pickle
from typing import Annotated

from fastapi import APIRouter, Depends, Response
from fastapi.responses import JSONResponse

from models.wagon import Wagon
from schemas.station import StationDocument
from schemas.user import UserDocument
from routes.deps import get_user
from util.build_path import get_shortest_path

from init_server import redis_db
from util.overpass import find_path

import itertools
from geopy import distance

from util.train_coords import get_mean_time, calculate_coords

trains_router = APIRouter(
    prefix="/trains",
    tags=["trains"]
)


@trains_router.post("/wagon/{wagon_id}")
async def add_wagon(body: Wagon):
    body.operdate = datetime.now()  # Set current time as start time

    pickled_wagon = pickle.dumps(body)
    redis_db.hset(name="wagon", key=body.wagon_id, value=pickled_wagon)

    return Response(status_code=200)


@trains_router.get("/wagon/")
async def get_all_wagons():
    result = []
    for wagon in redis_db.hscan_iter(name="wagon"):
        wagon_data = pickle.loads(wagon[1])
        result.append(wagon_data.to_json())

    return JSONResponse(content=result, status_code=200)


@trains_router.get("/wagon/{wagon_id}")
async def get_wagon(wagon_id: int):
    cache = redis_db.hget(name="wagon", key=wagon_id)

    if cache is None:
        return JSONResponse(content=f"Wagon with {wagon_id=} was not found", status_code=404)

    wagon = pickle.loads(cache)
    return JSONResponse(content=wagon.to_json(), status_code=200)


@trains_router.get("/train/{train_id}")
async def get_train(train_id: str):
    wagons = []
    for wagon in redis_db.hscan_iter(name="wagon"):
        wagon_data = pickle.loads(wagon[1])
        if wagon_data.train_index == train_id:
            wagons.append(wagon_data)

    if len(wagons) == 0:
        return JSONResponse(status_code=404, content=f"Train with {train_id=} was not found")

    start_node_id = wagons[0].st_id_disl
    end_node_id = int(train_id.split("-")[2])
    end_node_id = get_shortest_path(start_node_id, end_node_id)[1]

    cache = redis_db.hget(name="train_path", key=train_id)

    if cache is not None:
        json_paths = json.loads(cache)
        path, cumulative_distances = json_paths["coords_path"], json_paths["cumulative_distances"]
    else:
        start_node = await StationDocument.by_id(start_node_id)
        end_node = await StationDocument.by_id(end_node_id)

        path = await find_path(start_node.coordinates.get_coords(), end_node.coordinates.get_coords())

        path = list(itertools.chain.from_iterable([way["geometry"] for way in path]))
        path = [[coord['lat'], coord['lon']] for coord in path]

        cumulative_distances = list(
            itertools.accumulate([distance.distance(previous, current).km for previous, current in
                                  zip(path[:-1], path[1:])]))

        json_paths = {"coords_path": path, "cumulative_distances": cumulative_distances}

        redis_db.hset(name="train_path", key=train_id, value=json.dumps(json_paths))

    # mean_time = get_mean_time(start_node_id, end_node_id, cumulative_distances[-1])
    time_stamp = datetime.now().timestamp() - wagons[0].operdate.timestamp()

    coords = calculate_coords(coords_path=path, cumulative_distances=cumulative_distances,
                              timestamp=time_stamp)

    return JSONResponse(status_code=200, content={
        "index": train_id,
        "position": [coords[0], coords[1]],
        "route": {
            "start": start_node_id,
            "end": end_node_id
        },
        "velocity": {
            "x": coords[2],
            "y": coords[3]
        },
        "wagons": [wagon.to_json() for wagon in wagons]
    })


@trains_router.get("/path")
async def get_path(station_1: int, station_2: int, user: Annotated[UserDocument, Depends(get_user)]):
    return JSONResponse(content={"way": get_shortest_path(station_1, station_2)})
