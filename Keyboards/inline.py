from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def start_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()

    kb.button(text = 'Команды', callback_data = 'command'), 
    kb.button(text = 'Добавить бота в чат', callback_data = 'insert_bot_the_chat')
    return kb.as_markup()