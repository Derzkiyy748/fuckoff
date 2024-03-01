#   МОДУЛИ
#-------------------------------------------------------------#
import config

from aiogram.types import Message, CallbackQuery, Union
from aiogram.filters import BaseFilter
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   КЛАСС ФИЛЬТР СООБЩЕНИЙ И КНОПОК
#-------------------------------------------------------------#
class Filter(BaseFilter):
    def __init__(self, chat: Union[str, list]):
        self.chat = chat

    async def __call__(self, obj) -> bool:
        if isinstance(obj, Message):
            return self.check_message(obj)
        elif isinstance(obj, CallbackQuery):
            return self.check_callback_query(obj)
        else:
            return False

    def check_message(self, message: Message) -> bool:
        if isinstance(self.chat, str):
            return message.chat.type == self.chat
        else:
            return message.chat.type in self.chat

    def check_callback_query(self, call: CallbackQuery) -> bool:
        if isinstance(self.chat, str):
            return call.message.chat.type == self.chat
        else:
            return call.message.chat.type in self.chat
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   ФИЛЬТР АДМИНА
#-------------------------------------------------------------# 
class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == config.admin_id
#-------------------------------------------------------------#
#-------------------------------------------------------------#