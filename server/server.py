from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from init_server import init_db
from routes.auth import auth_router
from routes.mail import mail_router
from routes.register import register_router
from routes.web_socket import ws_router
from routes.trains import trains_router

app = FastAPI(
    title="DataWagonApp",
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(mail_router)
app.include_router(register_router)
app.include_router(trains_router)
app.include_router(ws_router)


@app.on_event("startup")
async def start_db():
    await init_db()
