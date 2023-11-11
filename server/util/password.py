import bcrypt


def hash_password(password: str) -> str:
    """Return a salted password hash."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_password(password: str, hashed_password: str) -> bool:
    """Check password match."""
    return bcrypt.checkpw(password.encode(), hashed_password.encode())
