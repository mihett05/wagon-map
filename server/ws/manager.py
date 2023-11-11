from fastapi import WebSocket

from ws.types import WsUserData


class ConnectionManager:
    connections: dict[WebSocket, WsUserData]

    def __init__(self):
        self.connections = {}

    def add(self, websocket: WebSocket) -> WsUserData:
        self.connections[websocket] = WsUserData(south_west=(0, 0), north_east=(0, 0))
        return self.connections[websocket]

    def remove(self, websocket: WebSocket):
        self.connections.pop(websocket)
