from aiogram.types import Message


async def is_reply_from_bot(message: Message) -> bool:
    reply = message.reply_to_message
    return reply and reply.from_user and reply.from_user.is_bot