#   ИМПОРТЫ
#-------------------------------------------------------------#
import config

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   ФУНКЦИИ КНОПОК ИНЛАЙН БЛОКА
#-------------------------------------------------------------#
def start_kb():
    kb = [
        [
            InlineKeyboardButton(text = 'Команды', callback_data = 'command'),
        ],
        [
            InlineKeyboardButton(text = 'Добавить бота в чат', url='https://t.me/ChillDinoGame_bot?startgroup=start')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard


def profile_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()

    kb.button(text = 'Получить жизни и удары', url=config.link)
    return kb.as_markup()


def profile_kb_1():
    kb = [
        [
            InlineKeyboardButton(text = 'Обновить профиль', callback_data = 'update_profile')
        ],
        [
            InlineKeyboardButton(text = 'Получить бонус жизни/удары', callback_data = 'bonus')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard
#-------------------------------------------------------------#
#-------------------------------------------------------------#


def menu_kb():
    kb = [
        [
            InlineKeyboardButton(text = 'Мой профиль', callback_data = 'profile')
        ],
        [
            InlineKeyboardButton(text = 'Команды', callback_data = 'command')
        ],
        [
            InlineKeyboardButton(text = 'Помощь', callback_data= 'support')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard