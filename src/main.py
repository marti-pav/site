from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import subprocess
from contextlib import asynccontextmanager

from src.config import Settings
from src.routes import router

settings = Settings()

@asynccontextmanager
async def lifespan(app):
    """Context manager for FastAPI app. It will run all code before `yield`
    on app startup, and will run code after `yeld` on app shutdown.
    """

    try:
        subprocess.run([
            "tailwindcss",
            "-i",
            "src/static/src/input.css",
            "-o",
            "src/static/css/main.css"
        ])
    except Exception as e:
        print(f"Error running tailwindcss: {e}")

    yield

def get_app() -> FastAPI:
    app = FastAPI(**settings.fastapi_kwargs, lifespan=lifespan)

    app.include_router(router)
    app.mount("/static", StaticFiles(directory="src/static"), name="static")

    return app


app = get_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)