from fastapi import HTTPException
from app.domain.models import User, UserLogin
from app.repository.cognito_repository import CognitoRepository

class AuthService:
    def __init__(self):
        self.repo = CognitoRepository()

    def register_user(self, user: User):
        try:
            response = self.repo.sign_up_user(user.username, user.password, user.email)
            return {"message": "User registered successfully", "response": response}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def login_user(self, user_login: UserLogin):
        try:
            token = self.repo.login_user(user_login.username, user_login.password)
            return {"access_token": token}
        except Exception as e:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
