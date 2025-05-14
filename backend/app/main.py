from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import user, anime
from .exception_handlers import add_exception_handlers

app = FastAPI(title="AnimeHub API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, restrict origins!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/api/user", tags=["user"])
app.include_router(anime.router, prefix="/api/anime", tags=["anime"])

add_exception_handlers(app)

@app.get("/")
async def root():
    return {"msg": "AnimeHub API running!"}