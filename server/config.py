import os

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    MONGO_URL: str = "mongodb://localhost:27017/db"
    INIT_DB_VALUES: bool = os.getenv('INIT_DB_VALUES', default=False)
    REDIS_HOST: str = os.getenv('REDIS_HOST', default="0.0.0.0")
    REDIS_PORT: int = int(os.getenv('REDIS_PORT', default=6379))

    # Security settings
    AUTH_JWT_SECRET_KEY: str = os.getenv("SECRET_KEY", default="89F4994C137BA7315508FF36999381F50E2C111BB436EE27EC3847D215CE4A51")

    # FastMail SMTP server settings
    MAIL_CONSOLE: bool = os.getenv("MAIL_CONSOLE", default=False)
    MAIL_SERVER: str = os.getenv("MAIL_SERVER", default="smtp.myserver.io")
    MAIL_PORT: int = os.getenv("MAIL_PORT", default=587)
    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME", default="")
    MAIL_PASSWORD: str = os.getenv("MAIL_PASSWORD", default="")
    MAIL_SENDER: str = os.getenv("MAIL_SENDER", default="noreply@myserver.io")


config = Config()
