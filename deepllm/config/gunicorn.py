import logging
import multiprocessing

from rich.console import Console
from rich.logging import RichHandler

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2
worker_class = "deepllm.config.uvicorn.UvicornWorker"

# Rich logging configuration
console = Console(force_terminal=True)
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console, rich_tracebacks=True)],
)

# Logging configuration
logconfig_dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "rich_console": {
            "class": "rich.logging.RichHandler",
            "console": console,
            "rich_tracebacks": True,
            "tracebacks_show_locals": True,
            "show_time": True,
            "show_level": True,
            "show_path": True,
        }
    },
    "loggers": {
        "gunicorn.error": {"handlers": ["rich_console"], "level": "INFO", "propagate": False},
        "gunicorn.access": {"handlers": ["rich_console"], "level": "INFO", "propagate": False},
    },
    "root": {"handlers": ["rich_console"], "level": "INFO"},
}

# Enable access log
accesslog = "-"  # stdout
errorlog = "-"  # stderr
loglevel = "info"
