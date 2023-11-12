from datetime import timedelta

from pydantic import BaseModel

from jwt import ACCESS_EXPIRES, REFRESH_EXPIRES
from models.user import UserRole


class AccessToken(BaseModel):
    access_token: str
    access_token_expires: timedelta = ACCESS_EXPIRES


class RefreshToken(AccessToken):
    refresh_token: str
    refresh_token_expires: timedelta = REFRESH_EXPIRES
    user_role: UserRole
