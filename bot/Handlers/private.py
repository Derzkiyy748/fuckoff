#   ИМПОРТЫ
#-------------------------------------------------------------#
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router, Bot
from modules.Filters import Filter
from database.requests import score_rang, update_bonus_user, select_user
from modules.profile import profile_user_1, profile_user_update
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   СОЗДАНИЕ ОБЪЕКТА РОУТЕРА
#-------------------------------------------------------------#
router_private = Router()
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   ОБРАБОТЧИК СПИСКА ПРОФИЛЬ
#-------------------------------------------------------------#
@router_private.callback_query(F.data == 'profile', Filter(chat=["private"]))
async def profile(call: CallbackQuery, bot: Bot) -> str:
    user_id = call.from_user.id
    next_rank = await score_rang(user_id)
    profile = await profile_user_1(user_id, bot, call, int(next_rank))
    
    return profile
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   ОБРАБОТЧИК БОНУСА
#-------------------------------------------------------------#
@router_private.callback_query(F.data == 'bonus', Filter(chat=["private"]))
async def bonus(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    user = await select_user(user_id)
    user_rank = user.rank
    bonus = await update_bonus_user(user_id, user_rank)

    if bonus and bonus[0] == True:
        await call.answer(f"Бонус за игру: {bonus[1]} ударов\n{bonus[2]} жизней", show_alert=True)
    else:
        await call.answer("Нет бонусов 😢\nПриходите через 24ч", show_alert=True)
#-------------------------------------------------------------#
#-------------------------------------------------------------#
        



@router_private.callback_query(F.data == 'update_profile', Filter(chat=["private"]))
async def update_profile(call: CallbackQuery, bot: Bot):

    user_id = call.from_user.id
    next_rank = await score_rang(user_id)
    profile = await profile_user_update(user_id, bot, call, int(next_rank))

    return profile
    
    
    
    

    