from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional
from datetime import datetime
from .base import TimestampMixin

class UserBase(BaseModel):
    username: str
    email: EmailStr
    display_name: Optional[str] = None
    profile_picture_url: Optional[HttpUrl] = None
    bio: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase, TimestampMixin):
    user_id: int
    is_active: bool = True
    is_verified: bool = False
    last_login_at: Optional[datetime] = None

    class Config:
        orm_mode = True