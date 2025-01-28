import pytest
from httpx import ASGITransport, AsyncClient

from deepllm.httpapi.app import app


@pytest.fixture()
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as async_client:
        yield async_client
