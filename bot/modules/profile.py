#   МОДУЛИ
#-------------------------------------------------------------#
from config import photo_rank
from datetime import datetime
from io import BytesIO
from PIL import Image
from aiogram import Bot
from aiogram.types import Message, FSInputFile, CallbackQuery
from database.requests import get_user, bonus_t
from Keyboards.inline import profile_kb, profile_kb_1
from message import profile_text, profile_text_private
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ ГРУППА
#-------------------------------------------------------------#
async def profile_user(user_id: int, bot: Bot, message: Message, next_rang: int):
    try:
        profile = await get_user(user_id)
        rank = profile.rank
        r = photo_rank[rank]
        filename = FSInputFile(r)

        if filename:
                await message.reply_photo(
                    photo= filename,
                    caption=profile_text(profile, next_rang),
                    parse_mode='html',
                    reply_markup=profile_kb()
                )
        else:
            await message.reply(
                profile_text(profile, next_rang),
                parse_mode='html',
                reply_markup=profile_kb()
            )
    except Exception as e:
        # Handle exceptions appropriately
        print(f"An error occurred: {e}")


#-------------------------------------------------------------#
#-------------------------------------------------------------#
        

#   ПРОФИЛЬ ДЛЯ ЛИЧНЫХ СООБЩЕНИЙ
#-------------------------------------------------------------#
async def profile_user_1(user_id: int, bot: Bot, call: CallbackQuery, next_rang: int):
    try:
        profile = await get_user(user_id)
        bonus = await bonus_t(user_id)
        photos = await bot.get_user_profile_photos(user_id)

        time_remaining = await bonus_t(user_id)
        

        if photos.photos:
            user_photo_path = photos.photos[0][-1].file_id
            await bot.send_photo(
                user_id,
                user_photo_path,
                caption=profile_text_private(profile, next_rang, str(time_remaining)),
                parse_mode='html',
                reply_markup=profile_kb_1()
            )
        else:
            await bot.send_message(
                user_id,
                profile_text_private(profile, next_rang, str(time_remaining)),
                parse_mode='html',
                reply_markup=profile_kb_1()
            )
    except Exception as e:
        print(f"Error in send_user_profile function: {e}")
#-------------------------------------------------------------#
#-------------------------------------------------------------#
        

async def profile_user_update(user_id: int, bot: Bot, call: CallbackQuery, next_rang: int):
    try:
        profile = await get_user(user_id)
        photos = await bot.get_user_profile_photos(user_id)
        time_remaining = await bonus_t(user_id)

        if photos.photos:
            user_photo_path = photos.photos[0][-1].file_id
            await bot.edit_message_caption(
                chat_id=user_id,
                message_id=call.message.message_id,  # Replace this with the actual message ID
                caption=profile_text_private(profile, next_rang, str(time_remaining)),
                parse_mode='html',
                reply_markup=profile_kb_1()
            )
        else:
            await bot.edit_message_text(
                chat_id=user_id,
                message_id=call.message.message_id,  # Replace this with the actual message ID
                text=profile_text_private(profile, next_rang, str(time_remaining)),
                parse_mode='html',
                reply_markup=profile_kb_1()
            )

    except Exception as e:
        print(f"Error in profile_user_update function: {e}")