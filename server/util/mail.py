from fastapi_mail import FastMail, ConnectionConfig, MessageSchema, MessageType

from config import config

mail_conf = ConnectionConfig(
    MAIL_USERNAME=config.MAIL_USERNAME,
    MAIL_PASSWORD=config.MAIL_PASSWORD,
    MAIL_FROM=config.MAIL_SENDER,
    MAIL_PORT=config.MAIL_PORT,
    MAIL_SERVER=config.MAIL_SERVER,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
)

mail = FastMail(mail_conf)

ROOT_URL = f"http://{config.SERVER_HOST}:{config.SERVER_PORT}"


async def send_verification_email(email: str, token: str) -> None:
    """Send user verification email."""
    # Change this later to public endpoint
    url = ROOT_URL + "/mail/verify/" + token
    if config.MAIL_CONSOLE:
        print("POST to " + url)
    else:
        message = MessageSchema(
            recipients=[email],
            subject="MyServer Email Verification",
            body=f"Welcome to MyServer! We just need to verify your email to begin: {url}",
            subtype=MessageType.plain,
        )
        await mail.send_message(message)


async def send_password_reset_email(email: str, token: str) -> None:
    """Send password reset email."""
    # Change this later to public endpoint
    url = ROOT_URL + "/register/reset-password/" + token
    if config.MAIL_CONSOLE:
        print("POST to " + url)
    else:
        message = MessageSchema(
            recipients=[email],
            subject="MyServer Password Reset",
            body=f"Click the link to reset your MyServer account password: {url}\nIf you did not request this, please "
                 f"ignore this email",
            subtype=MessageType.plain,
        )
        await mail.send_message(message)
