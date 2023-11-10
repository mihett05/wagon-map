from pymongo.errors import DuplicateKeyError
from fastapi import APIRouter, WebSocket, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from init_server import redis_db
from models.train import Train
from schemas.train import TrainDocument

# from routes.web_socket import ConnectionManager, RequestHandler

basic_router = APIRouter(
    prefix="/basic",
    tags=["basic"]
)

# manager = ConnectionManager()

# @router.websocket("/trains")
# async def ws_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     manager.add(websocket)
#     handler = RequestHandler(websocket)
#     while True:
#         data = await websocket.receive_json()
#         request = request_type(**data)
#         response = await handler.handle(request)
#         await websocket.send_text(response.model_dump_json())


@basic_router.get("/test_redis")
async def test_redis(test_key: str, test_value: str):
    cache = redis_db.hget(name="wagon", key=test_key)

    redis_db.hset(name="wagon", key=test_key, value=test_value)

    if cache is not None:
        return JSONResponse(content=f"Key was found: {cache}")

    return JSONResponse(content=f"Key was not found")


@basic_router.post("/test_mongo")
async def test_mongo(body: Train):
    train = TrainDocument(**{
        "train_info": body
    })
    try:
        await train.create()
    except DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Train already exists",
        )
    return train
