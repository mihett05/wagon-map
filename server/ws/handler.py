import asyncio
from inspect import getfullargspec
from opcode import hasjabs
from fastapi import WebSocket

from .types import EventType, Request, Response, WsUserData
from .manager import ConnectionManager


class SendResponse:
    def __init__(self, request: Request, websocket: WebSocket):
        self.request = request
        self.websocket = websocket

    def update_response(self, response: Response):
        response.uid = self.request.uid
        response.event = self.request.event

    async def send(self, response: Response):
        self.update_response(response)
        await self.websocket.send_text(response.model_dump_json())


class EventHandler:
    def __init__(self, event_type: EventType):
        self.type = event_type
        self.request_type = None
        self.response_type = None
        self.handlers = []

    def request(self, cls):
        self.request_type = cls
        return cls

    def response(self, cls):
        self.response_type = cls
        return cls

    def handler(self, func):
        self.handlers.append(func)
        return func

    async def run(
        self,
        event: EventType,
        data: dict,
        websocket: WebSocket,
        manager: ConnectionManager,
        user_data: WsUserData,
    ):
        if event != self.type:
            return
        if not self.request_type or not issubclass(self.request_type, (Request,)):
            raise ValueError(f"'{self.type}' handler has invalid 'request_type'")

        request = self.request_type(**data)
        send_response = SendResponse(request, websocket)

        deps = {
            self.request_type: request,
            WebSocket: websocket,
            ConnectionManager: manager,
            SendResponse: send_response,
            WsUserData: user_data,
        }
        # TODO: добавить User в DI
        # TODO: добавить чё-то типа подписки на обновление поездов в DI

        for handler in self.handlers:
            annotations = getfullargspec(handler).annotations
            return_type = annotations.pop("return", None)
            kwargs = {}

            for arg, t in annotations.items():
                for cls in deps:
                    if issubclass(t, cls):
                        kwargs[arg] = deps[cls]
            await handler(**kwargs)
            # asyncio.create_task(handler(**kwargs))
