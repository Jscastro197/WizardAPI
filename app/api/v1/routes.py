from fastapi import APIRouter, Depends
from app.domain.models import User, UserLogin
from app.services.auth_service import AuthService

router = APIRouter()
auth_service = AuthService()

@router.post("/signup")
def signup(user: User):
    return auth_service.register_user(user)

@router.post("/login")
def login(user_login: UserLogin):
    return auth_service.login_user(user_login)