from aiogram.types import Message, CallbackQuery
from aiogram import F, filters, Router, Bot
from aiogram.filters import CommandStart, Command
from modules.Filters import Filter
from database.requests import score_rang
from modules.profile import profile_user_1


router = Router()


@router.message(F.text.in_(['п', 'профиль', 'Профиль', 'П']), Filter(chat=["private"]))
async def profile(message: Message, bot: Bot) -> str:
    user_id = message.from_user.id
    next_rank = await score_rang(user_id)
    profile = await profile_user_1(user_id, bot, message, int(next_rank))
    
    return profile


@router.message(F.data == 'bonus', Filter(chat=["private"]))
async def bonus(message: Message, bot: Bot):
   ...
    