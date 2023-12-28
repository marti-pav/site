from pathlib import Path
from typing import Any

from fastapi.responses import HTMLResponse
from pydantic_settings import BaseSettings
from typing import Any

APP_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):

    APP_DIR: Path = APP_DIR

    DATA_DIR: Path = APP_DIR.parent / 'data'
    STATIC_DIR: Path = APP_DIR / 'static'
    TEMPLATE_DIR: Path = APP_DIR / 'templates'

    FASTAPI_PROPERTIES: dict[str, Any] = {
        "title": "Simple Site",
        "description": "A simple htmx and tailwind site built with FastAPI",
        "version": "0.0.1",
        "default_response_class": HTMLResponse
    }

    DISABLE_DOCS: bool = True

    @property
    def fastapi_kwargs(self) -> dict[str, Any]:
        fastapi_kwargs = self.FASTAPI_PROPERTIES
        if self.DISABLE_DOCS:
            fastapi_kwargs.update(
                {
                    "openapi_url": None,
                    "openapi_prefix": None,
                    "docs_url": None,
                    "redoc_url": None,
                }
            )
        return fastapi_kwargs



