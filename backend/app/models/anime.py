from pydantic import BaseModel
from typing import Optional
from datetime import date
from .base import TimestampMixin
from .enums import AnimeType, AnimeStatus

class AnimeBase(BaseModel):
    title_romaji: str
    title_english: Optional[str] = None
    title_japanese: Optional[str] = None
    synopsis: Optional[str] = None
    type: AnimeType = AnimeType.TV
    source: Optional[str] = None
    episodes: Optional[int] = None
    status: AnimeStatus = AnimeStatus.NOT_YET_AIRED

class AnimeCreate(AnimeBase):
    pass

class AnimeInDB(AnimeBase, TimestampMixin):
    anime_id: int
    average_score: float = 0.0
    score_count: int = 0
    popularity_rank: Optional[int] = None
    members_count: int = 0
    favorites_count: int = 0

    class Config:
        orm_mode = True