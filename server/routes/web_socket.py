from fastapi import APIRouter, WebSocket
from pydantic import ValidationError
from ws.manager import ConnectionManager
from ws.events import handlers
from ws.types import Request


ws_router = APIRouter(prefix="/websocket", tags=["websocket", "trains"])

manager = ConnectionManager()


@ws_router.websocket("/")
async def ws_endpoint(websocket: WebSocket):
    # TODO: auth
    await websocket.accept()
    user_data = manager.add(websocket)
    while True:
        data = await websocket.receive_json()
        try:
            event = Request(**data).event
            await handlers[event].run(
                event,
                data,
                websocket,
                manager,
                user_data,
            )
        except ValidationError:
            await websocket.send_json({"error": "Invalid request"})
