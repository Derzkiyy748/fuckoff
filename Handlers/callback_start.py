from aiogram import Bot, types, F, Router
from aiogram.types import Message, CallbackQuery
from message import commands_text
from aiogram.types import ChatMemberUpdated


call_router = Router()
call_router.message.filter(F.chat.type == "group")


@call_router.callback_query(F.data == "command")
async def command(call: CallbackQuery, bot: Bot):
    await call.message.reply(commands_text())


@call_router.callback_query(F.data == "insert_bot_the_chat")
async def insert_bot_the_chat(call: CallbackQuery, bot: Bot):
    # Получаем информацию о члене чата (user, chat, etc.)
    chat_member_updated: ChatMemberUpdated = call.chat_member_updated
    if chat_member_updated.new_chat_member and chat_member_updated.new_chat_member.is_bot:
        chat_id = call.message.chat.id
        bot_id = chat_member_updated.new_chat_member.user.id

        # Ваш код для обработки добавления бота в чат
        print(f"Бот с ID {bot_id} добавлен в чат с ID {chat_id}")


