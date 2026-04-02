import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    aws_region: str = os.getenv("AWS_REGION", "us-west-2")
    cognito_user_pool_id: str = os.getenv("COGNITO_USER_POOL_ID")
    cognito_client_id: str = os.getenv("COGNITO_CLIENT_ID")

settings = Settings()