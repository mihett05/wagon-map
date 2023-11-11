from models.train import Train
from ws.handler import EventHandler, SendResponse
from ws.types import EventType, Request, Response
from ws.types import WsUserData


handler = EventHandler(EventType.UPDATE_BOUNDS)


@handler.request
class UpdateBoundsRequest(Request):
    south_west: tuple[float, float]
    north_east: tuple[float, float]


@handler.response
class UpdateBoundsResponse(Response):
    trains: list[Train]


@handler.handler
async def handle(request: UpdateBoundsRequest, send: SendResponse, data: WsUserData):
    data.north_east = request.north_east
    data.south_west = request.south_west
    # TOOD: сделать фильтрацию
    response = UpdateBoundsResponse(trains=[])
    await send.send(response)
