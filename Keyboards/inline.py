from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def start_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()

    kb.button(text = 'Команды', callback_data = 'command'), 
    kb.button(text = 'Добавить бота в чат', url='https://t.me/ChillDinoGame_bot?startgroup=start')
    return kb.as_markup()


def profile_kb(user_id: int) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()

    kb.button(text = 'Получить жизни и удары', url='https://telegra.ph/KAK-POLUCHIT-ZHIZNI-I-UDARY-V-BOTE-02-24')
    return kb.as_markup()