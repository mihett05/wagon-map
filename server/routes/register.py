from fastapi import APIRouter, Body, HTTPException, Response
from pydantic import EmailStr

from models.user import UserOut, UserRole, AdminUserAuth
from schemas.user import UserDocument
from jwt import access_security, user_from_token
from util.mail import send_password_reset_email
from util.password import hash_password

register_router = APIRouter(prefix="/register", tags=["Register"])

embed = Body(..., embed=True)


@register_router.post("", response_model=UserOut)
async def register_operator(admin_user_auth: AdminUserAuth):  # type: ignore[no-untyped-def]
    # Verify admin role
    user = await user_from_token(admin_user_auth.token)
    if user is None:
        raise HTTPException(404, "No user found with that email")
    if user.email_confirmed_at is None:
        raise HTTPException(400, "Email is not yet verified")
    if user.disabled:
        raise HTTPException(400, "Your account is disabled")
    if user.role != UserRole.ADMIN:
        raise HTTPException(403, "Permission denied")

    """Create a new user."""
    user = await UserDocument.by_email(admin_user_auth.email)
    if user is not None:
        raise HTTPException(409, "User with that email already exists")
    hashed = hash_password(admin_user_auth.password)
    user = UserDocument(email=admin_user_auth.email, password=hashed, role=UserRole.OPERATOR)
    await user.create()
    return user


@register_router.post("/forgot-password")
async def forgot_password(email: EmailStr = embed) -> Response:
    """Send password reset email."""
    user = await UserDocument.by_email(email)
    if user is None:
        raise HTTPException(404, "No user found with that email")
    if user.email_confirmed_at is not None:
        raise HTTPException(400, "Email is already verified")
    if user.disabled:
        raise HTTPException(400, "Your account is disabled")
    token = access_security.create_access_token(user.jwt_subject)
    await send_password_reset_email(email, token)
    return Response(status_code=200)


@register_router.post("/reset-password/{token}", response_model=UserOut)
async def reset_password(token: str, password: str = embed):  # type: ignore[no-untyped-def]
    """Reset user password from token value."""
    user = await user_from_token(token)
    if user is None:
        raise HTTPException(404, "No user found with that email")
    if user.email_confirmed_at is None:
        raise HTTPException(400, "Email is not yet verified")
    if user.disabled:
        raise HTTPException(400, "Your account is disabled")
    user.password = hash_password(password)
    await user.save()
    return user
