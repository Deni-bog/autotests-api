from httpx import Response
from clients.public_http_builder import get_public_http_client

from clients.api_client import APIClient
from typing import TypedDict

class Token(TypedDict):
    tokenType: str
    accessToken: str
    refreshToken: str


class LoginResponseDict(TypedDict):
    token: Token

class LoginRequestDict(TypedDict):
    email: str
    password: str

class RefreshRequestDict(TypedDict):
    refreshToken :str

class AuthenticationClient(APIClient):


    def login_api(self, request: LoginRequestDict) -> Response:
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        return self.post("/api/v1/authentication/refresh", json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        response = self.login_api(request)
        return response.json()

def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client = get_public_http_client())

