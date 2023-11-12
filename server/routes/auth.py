from fastapi import APIRouter, HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials

from models.auth import RefreshToken, AccessToken
from models.user import UserAuth
from schemas.user import UserDocument
from jwt import access_security, refresh_security
from util.password import check_password


auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/login")
async def login(user_auth: UserAuth) -> RefreshToken:
    """Authenticate and returns the user's JWT."""
    user = await UserDocument.by_email(user_auth.email)
    if user is None or not check_password(password=user_auth.password, hashed_password=user.password):
        raise HTTPException(status_code=401, detail="Bad email or password")
    if user.email_confirmed_at is None:
        raise HTTPException(status_code=400, detail="Email is not yet verified")
    access_token = access_security.create_access_token(user.jwt_subject)
    refresh_token = refresh_security.create_refresh_token(user.jwt_subject)
    return RefreshToken(access_token=access_token, refresh_token=refresh_token, user_role=user.role)


@auth_router.post("/refresh")
async def refresh(
    auth: JwtAuthorizationCredentials = Security(refresh_security)
) -> AccessToken:
    """Return a new access token from a refresh token."""
    access_token = access_security.create_access_token(subject=auth.subject)
    return AccessToken(access_token=access_token)
