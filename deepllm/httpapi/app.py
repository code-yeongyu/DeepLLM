from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from deepllm.httpapi.health.router import router as health_router

app = FastAPI(
    default_response_class=ORJSONResponse,
    title="DeepLLM API",
    description="DeepLLM: Leverage reasoning LLMs to get decent responses.",
)

app.include_router(health_router)
