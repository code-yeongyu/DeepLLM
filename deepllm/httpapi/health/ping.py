from typing import Literal

from pydantic import BaseModel

from deepllm.httpapi.health.router import router


class PingSchema(BaseModel):
    message: Literal["pong"]


@router.get("/ping", status_code=200, summary="Ping endpoint", response_description="Returns a pong message")
async def ping() -> PingSchema:
    return PingSchema(message="pong")
