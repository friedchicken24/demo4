from ..database import get_db
from ..models.users import UserCreate, UserInDB
from ..utils.security import hash_password
from fastapi import HTTPException
import pymysql

def create_user(user: UserCreate):
    with get_db() as db:
        with db.cursor() as cursor:
            cursor.execute("SELECT user_id FROM users WHERE username=%s OR email=%s", (user.username, user.email))
            if cursor.fetchone():
                raise HTTPException(status_code=400, detail="Username or email exists")
            cursor.execute(
                "INSERT INTO users (username, email, password_hash, display_name, is_active, is_verified) VALUES (%s, %s, %s, %s, %s, %s)",
                (user.username, user.email, hash_password(user.password), user.display_name, True, False)
            )
            user_id = cursor.lastrowid
            db.commit()
            return UserInDB(
                user_id=user_id, username=user.username, email=user.email,
                display_name=user.display_name, is_active=True, is_verified=False,
                last_login_at=None, created_at=None, updated_at=None
            )