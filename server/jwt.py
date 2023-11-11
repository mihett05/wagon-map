from datetime import timedelta

from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer, JwtRefreshBearer

from config import config
from schemas.user import UserDocument

ACCESS_EXPIRES = timedelta(minutes=15)
REFRESH_EXPIRES = timedelta(days=30)

access_security = JwtAccessBearer(
    config.AUTH_JWT_SECRET_KEY,
    access_expires_delta=ACCESS_EXPIRES,
    refresh_expires_delta=REFRESH_EXPIRES,
)

refresh_security = JwtRefreshBearer(
    config.AUTH_JWT_SECRET_KEY,
    access_expires_delta=ACCESS_EXPIRES,
    refresh_expires_delta=REFRESH_EXPIRES,
)


async def user_from_credentials(auth: JwtAuthorizationCredentials) -> UserDocument | None:
    """Return the user associated with auth credentials."""
    return await UserDocument.by_email(auth.subject["username"])


async def user_from_token(token: str) -> UserDocument | None:
    """Return the user associated with a token value."""
    payload = access_security._decode(token)
    return await UserDocument.by_email(payload["subject"]["username"])
