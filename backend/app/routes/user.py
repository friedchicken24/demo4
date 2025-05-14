from fastapi import APIRouter
from ..models.users import UserCreate, UserInDB
from ..controllers.user_controller import create_user

router = APIRouter()

@router.post("/register", response_model=UserInDB)
def register(user: UserCreate):
    return create_user(user)

