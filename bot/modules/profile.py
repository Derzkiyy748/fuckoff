#   МОДУЛИ
#-------------------------------------------------------------#
from aiogram import Bot
from aiogram.types import Message
from database.requests import get_user
from Keyboards.inline import profile_kb, profile_kb_1
from message import profile_text
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ ГРУППА
#-------------------------------------------------------------#
async def profile_user(user_id: int, bot: Bot, message: Message, next_rang: int):
    try:
        profile = await get_user(user_id)
        photos = await bot.get_user_profile_photos(user_id)
        if photos.photos:
            user_photo_path = photos.photos[0][-1].file_id
            await message.reply_photo(
                user_photo_path,
                caption=profile_text(profile, next_rang),
                parse_mode='html',
                reply_markup=profile_kb(user_id)
            )
        else:
            await message.reply(
                profile_text(profile, next_rang),
                parse_mode='html',
                reply_markup=profile_kb(user_id)
            )

    except Exception as e:
        print(f"Error in send_user_profile function: {e}")
#-------------------------------------------------------------#
#-------------------------------------------------------------#
        

#   ПРОФИЛЬ ДЛЯ ЛИЧНЫХ СООБЩЕНИЙ
#-------------------------------------------------------------#
async def profile_user_1(user_id: int, bot: Bot, message: Message, next_rang: int):
    try:
        profile = await get_user(user_id)
        photos = await bot.get_user_profile_photos(user_id)
        if photos.photos:
            user_photo_path = photos.photos[0][-1].file_id
            await message.reply_photo(
                user_photo_path,
                caption=profile_text(profile, next_rang),
                parse_mode='html',
                reply_markup=profile_kb_1(user_id)
            )
        else:
            await message.reply(
                profile_text(profile, next_rang),
                parse_mode='html',
                reply_markup=profile_kb_1(user_id)
            )

    except Exception as e:
        print(f"Error in send_user_profile function: {e}")
#-------------------------------------------------------------#
#-------------------------------------------------------------#