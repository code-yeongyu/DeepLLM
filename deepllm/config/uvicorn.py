from uvicorn.workers import UvicornWorker as BaseUvicornWorker


class UvicornWorker(BaseUvicornWorker):
    CONFIG_KWARGS = {
        **BaseUvicornWorker.CONFIG_KWARGS,
        "lifespan": "off",
        "proxy_headers": True,
    }
