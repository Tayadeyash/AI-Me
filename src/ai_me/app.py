"""Minimal service entrypoint."""

from fastapi import FastAPI

from ai_me import __version__

app = FastAPI(title="AI-Me", version=__version__)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "version": __version__}
