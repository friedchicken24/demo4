from fastapi import APIRouter
from ..models.anime import AnimeCreate, AnimeInDB
from ..controllers.anime_controller import create_anime

router = APIRouter()

@router.post("/", response_model=AnimeInDB)
def create(anime: AnimeCreate):
    return create_anime(anime)