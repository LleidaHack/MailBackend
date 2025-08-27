FROM python:3.11-slim

# Set working directory
WORKDIR /app

ARG GIT_BRANCH

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    curl \
    python3-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Clone the repository
RUN git clone https://github.com/LleidaHack/MailBackend.git . && \
    git checkout ${GIT_BRANCH}

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

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
  CMD curl -f http://localhost:8001/v1/health || exit 1

# Run migrations then start server
CMD ["sh", "-c", "uv run alembic upgrade head && uv run gunicorn main:app -c gunicorn_conf.py --bind 0.0.0.0:8001"]