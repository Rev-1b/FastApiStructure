from fastapi import FastAPI
import logging

from starlette.websockets import WebSocket

logger = logging.getLogger(__name__)

app = FastAPI()

USERS: dict[str, WebSocket] = {}


@app.get("/")
async def root():
    return {"message": "Hello World"}


