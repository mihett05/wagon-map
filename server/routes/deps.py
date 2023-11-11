from typing import Annotated, Optional
from fastapi import Header, HTTPException

from jwt import user_from_token
from schemas.station import StationDocument
from schemas.user import UserDocument


async def get_user(token: Annotated[Optional[str], Header()] = None) -> UserDocument:
    user = await user_from_token(token)
    if user is None:
        raise HTTPException(404, "No user found with that email")
    if user.email_confirmed_at is None:
        raise HTTPException(400, "Email is not verified")
    if user.disabled:
        raise HTTPException(400, "Your account is disabled")
    return user


async def get_station(id: int) -> StationDocument:
    station = await StationDocument.find_one(StationDocument.id == id)
    if station is None:
        raise HTTPException(404, f"No station found with {id=}")
    return station
