#   ИМПОРТЫ
#-------------------------------------------------------------#
import config

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   ФУНКЦИИ КНОПОК ИНЛАЙН БЛОКА
#-------------------------------------------------------------#
def start_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()

    kb.button(text = 'Команды', callback_data = 'command'), 
    kb.button(text = 'Добавить бота в чат', url='https://t.me/ChillDinoGame_bot?startgroup=start')
    return kb.as_markup()


def profile_kb(user_id: int) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()

    kb.button(text = 'Получить жизни и удары', url=config.link)
    return kb.as_markup()


def profile_kb_1(user_id: int) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()

    kb.button(text = 'Обновить профиль', callback_data = 'update_profile')
    kb.button(text = 'Получить бонус жизни/удары', callback_data = 'bonus')
    return kb.as_markup()
#-------------------------------------------------------------#
#-------------------------------------------------------------#