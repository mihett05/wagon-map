import uvicorn

from config import config

if __name__ == "__main__":
    uvicorn.run(
        "server:app", host=config.SERVER_HOST, port=config.SERVER_PORT, reload=False
    )
