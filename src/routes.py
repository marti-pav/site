from fastapi import APIRouter, Request
from jinja2_fragments.fastapi import Jinja2Blocks
from src.crud import CRUD

templates = Jinja2Blocks(directory="src/templates")
router = APIRouter()


@router.get("/")
def index(request: Request):
    db = CRUD().with_table("artist_info")
    random_artist = db.get_random_item()

    return templates.TemplateResponse("main.html",
      {
          "request": request,
          "random_artist": random_artist,
      })