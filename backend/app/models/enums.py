from enum import Enum

class AnimeType(str, Enum):
    TV = "TV"
    OVA = "OVA"
    ONA = "ONA"
    MOVIE = "Movie"
    SPECIAL = "Special"
    OTHER = "Other"

class AnimeStatus(str, Enum):
    NOT_YET_AIRED = "not_yet_aired"
    AIRING = "airing"
    FINISHED = "finished"
    CANCELLED = "cancelled"
    OTHER = "other"