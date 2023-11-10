from fastapi import WebSocket

from models.ws_data import WsUserData


class ConnectionManager:
    connections: [WebSocket, WsUserData]

    def __init__(self):
        self.connections = {}

    def add(self, websocket: WebSocket):
        self.connections[WebSocket] = WsUserData(south_west=(0, 0), north_east=(0, 0))

    def remove(self, websocket: WebSocket):
        self.connections.pop(websocket)


# class RequestHandler:
#     def __init__(self, websocket: WebSocket):  # on_connect
#         self.ws = websocket
#
#     async def handle(self, request: Request):
#         if request.request_type == RequestType.UPDATE_BOUNDS:  # потом при помощи декораторов сделаю нормально
#             manager[self.ws] = WsUserData(south_west=request.south_west, north_east=request.north_east)
#             # ... делаем фильтрацию
#             return UpdateBoundsResponse(...)
