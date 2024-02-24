from aiogram import Bot, types, F, Router
from aiogram.types import Message, CallbackQuery
from message import commands_text
from aiogram.types import ChatMemberUpdated


call_router = Router()
call_router.message.filter(F.chat.type == "group")


@call_router.callback_query(F.data == "command")
async def command(call: CallbackQuery, bot: Bot):
    await call.message.reply(commands_text())




