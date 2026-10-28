FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:0.12.7 /uv /bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --no-install-project
COPY main.py settings.py alembic.ini ./
COPY migrations ./migrations
ENV PATH="/app/.venv/bin:$PATH"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
