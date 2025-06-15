FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml ./
COPY src/ src/
COPY alembic/ alembic/
COPY alembic.ini ./
COPY main.py ./
COPY gunicorn_conf.py ./

# Create non-root user first
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

# Install dependencies with uv as the app user
RUN uv sync --no-cache

# Create logs directory
RUN mkdir -p logs

# Expose port
EXPOSE 8001

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8001/health || exit 1

# Run with gunicorn
CMD ["sh", "-c", "uv run gunicorn main:app -c gunicorn_conf.py --bind 0.0.0.0:8001"]