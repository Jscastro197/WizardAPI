# domain/domain.py

from pydantic import BaseModel, EmailStr
from pydantic_settings import BaseSettings

class User(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str