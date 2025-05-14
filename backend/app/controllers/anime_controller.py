from ..database import get_db
from ..models.anime import AnimeCreate, AnimeInDB
from fastapi import HTTPException

def create_anime(anime: AnimeCreate):
    with get_db() as db:
        with db.cursor() as cursor:
            cursor.execute(
                "INSERT INTO anime (title_romaji, title_english, title_japanese, synopsis, type, source, episodes, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (anime.title_romaji, anime.title_english, anime.title_japanese, anime.synopsis, anime.type.value, anime.source, anime.episodes, anime.status.value)
            )
            anime_id = cursor.lastrowid
            db.commit()
            return AnimeInDB(
                anime_id=anime_id, title_romaji=anime.title_romaji, title_english=anime.title_english,
                title_japanese=anime.title_japanese, synopsis=anime.synopsis, type=anime.type,
                source=anime.source, episodes=anime.episodes, status=anime.status,
                aired_from=None, aired_to=None, duration_per_episode=None, age_rating=None,
                cover_image_url=None, banner_image_url=None, youtube_trailer_id=None,
                average_score=0, score_count=0, popularity_rank=None, members_count=0, favorites_count=0,
                created_at=None, updated_at=None
            )