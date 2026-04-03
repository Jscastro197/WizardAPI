import base64
import hashlib
import hmac

import boto3
from botocore.exceptions import ClientError

from app.core.config import settings


class CognitoRepository:
    def __init__(self):
        self.client = boto3.client(
            "cognito-idp",
            region_name=settings.aws_region,
        )

    def generate_secret_hash(self, username: str) -> str:
        message = username + settings.cognito_client_id
        digest = hmac.new(
            settings.cognito_client_secret.encode("utf-8"),
            message.encode("utf-8"),
            hashlib.sha256,
        ).digest()
        return base64.b64encode(digest).decode("utf-8")

    def sign_up_user(self, username: str, password: str, email: str):
        try:
            response = self.client.sign_up(
                ClientId=settings.cognito_client_id,
                Username=username,
                Password=password,
                SecretHash=self.generate_secret_hash(username),
                UserAttributes=[{"Name": "email", "Value": email}],
            )
            return response
        except ClientError as e:
            raise e

    def login_user(self, username: str, password: str):
        try:
            response = self.client.initiate_auth(
                ClientId=settings.cognito_client_id,
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={
                    "USERNAME": username,
                    "PASSWORD": password,
                    "SECRET_HASH": self.generate_secret_hash(username),
                },
            )
            return response["AuthenticationResult"]["AccessToken"]
        except ClientError as e:
            raise e