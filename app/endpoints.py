from fastapi import APIRouter
from pydantic import BaseModel
from notifier.email_sender import Email 
from notifier.telegram_sender import Telegram

router = APIRouter(prefix="/send", tags=["send"])


class Message(BaseModel):
    recipient: str
    content: str


@router.post("/email")
async def send_email_message(message: Message):
    Email().send(message.recipient, message.content)
    return {"status": "Email sent"}


@router.post("/telegram")
async def send_telegram_message(message: Message):
    Telegram().send_message(message.recipient, message.content)
    return {"status": "Telegram message sent"}
