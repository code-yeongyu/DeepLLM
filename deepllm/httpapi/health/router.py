from fastapi import APIRouter

from deepllm.utils.relative_import import relative_import

router = APIRouter(tags=["health"])

relative_import(".ping")
