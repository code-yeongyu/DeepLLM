FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get upgrade -y

WORKDIR /app

# Copy project files
COPY . .

# Install dependencies using uv
RUN uv sync --compile-bytecode --no-dev --frozen

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application using Gunicorn
CMD ["uv", "run", "gunicorn", "deepllm.httpapi.app:app", "--config", "deepllm/config/gunicorn.py"]
