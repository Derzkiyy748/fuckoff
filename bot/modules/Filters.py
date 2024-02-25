from aiogram.types import Message, CallbackQuery, Union
from aiogram.filters import BaseFilter



class Filter(BaseFilter):  # [1]
    def __init__(self, chat: Union[str, list]): # [2]
        self.chat = chat

    async def __call__(self, message: Message) -> bool:  # [3]
        if isinstance(self.chat, str):
            return message.chat.type == self.chat
        else:
            return message.chat.type in self.chat