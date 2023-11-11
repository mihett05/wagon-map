from enum import Enum
from typing import Annotated

from beanie import Indexed
from pydantic import BaseModel, EmailStr


class UserRole(str, Enum):
    OPERATOR = "operator"
    ADMIN = "admin"


class UserAuth(BaseModel):
    """User register and login auth."""

    email: EmailStr
    password: str


class AdminUserAuth(UserAuth):
    token: str


class UserUpdate(BaseModel):
    """Updatable user fields."""

    email: EmailStr | None = None

    # User information
    first_name: str | None = None
    last_name: str | None = None


class UserOut(UserUpdate):
    """User fields returned to the client."""

    email: Annotated[str, Indexed(EmailStr, unique=True)]
    disabled: bool = False
