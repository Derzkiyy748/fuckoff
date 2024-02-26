from aiogram.types import Message, CallbackQuery
from aiogram import F, Router, Bot
from modules.Filters import Filter
from database.requests import score_rang, update_bonus_user, select_user
from modules.profile import profile_user_1


router_private = Router()


@router_private.message(F.text.in_(['п', 'профиль', 'Профиль', 'П']), Filter(chat=["private"]))
async def profile(message: Message, bot: Bot) -> str:
    user_id = message.from_user.id
    next_rank = await score_rang(user_id)
    profile = await profile_user_1(user_id, bot, message, int(next_rank))
    
    return profile


@router_private.callback_query(F.data == 'bonus', Filter(chat=["private"]))
async def bonus(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    user = await select_user(user_id)
    user_rank = user.rank
    bonus = await update_bonus_user(user_id, user_rank)

    if bonus and bonus[0] == True:
        await call.answer(f"Бонус за игру: {bonus[1]} ударов\n{bonus[2]} жизней", show_alert=True)
    else:
        await call.answer("Нет бонусов 😢", show_alert=True)
    
    

    