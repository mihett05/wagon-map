from datetime import datetime, UTC

from fastapi import APIRouter, Body, HTTPException, Response
from pydantic import EmailStr

from schemas.user import UserDocument
from jwt import access_security, user_from_token
from util.mail import send_verification_email


mail_router = APIRouter(prefix="/mail", tags=["Mail"])


@mail_router.post("/verify")
async def request_verification_email(
    email: EmailStr = Body(..., embed=True)
) -> Response:
    """Send the user a verification email."""
    user = await UserDocument.by_email(email)
    if user is None:
        raise HTTPException(404, "No user found with that email")
    if user.email_confirmed_at is not None:
        raise HTTPException(400, "Email is already verified")
    if user.disabled:
        raise HTTPException(400, "Your account is disabled")
    token = access_security.create_access_token(user.jwt_subject)
    await send_verification_email(email, token)
    return Response(status_code=200)


@mail_router.post("/verify/{token}")
async def verify_email(token: str) -> Response:
    """Verify the user's email with the supplied token."""
    user = await user_from_token(token)
    if user is None:
        raise HTTPException(404, "No user found with that email")
    if user.email_confirmed_at is not None:
        raise HTTPException(400, "Email is already verified")
    if user.disabled:
        raise HTTPException(400, "Your account is disabled")
    user.email_confirmed_at = datetime.now(tz=UTC)
    await user.save()
    return Response(status_code=200)


@mail_router.post("/simple_verify")
async def simple_verification(
    email: EmailStr = Body(..., embed=True)
) -> Response:
    """Send the user a verification email."""
    user = await UserDocument.by_email(email)
    if user is None:
        raise HTTPException(404, "No user found with that email")
    if user.email_confirmed_at is not None:
        raise HTTPException(400, "Email is already verified")
    if user.disabled:
        raise HTTPException(400, "Your account is disabled")
    user.email_confirmed_at = datetime.now(tz=UTC)
    await user.save()
    return Response(status_code=200)
