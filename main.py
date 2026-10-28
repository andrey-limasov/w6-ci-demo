import psycopg
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from settings import settings

app = FastAPI(title="w6-ci-demo", version="0.1.0")


@app.get("/health", response_model=None)
def health() -> dict[str, str] | JSONResponse:
    try:
        with psycopg.connect(settings.database_url, connect_timeout=3) as conn:
            conn.execute("SELECT 1")
    except psycopg.Error:
        return JSONResponse(status_code=503, content={"status": "unhealthy"})
    return {"status": "healthy"}


@app.get("/version")
def version() -> dict[str, str]:
    return {"version": app.version}
