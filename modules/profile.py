from aiogram import Bot
from aiogram.types import Message
from database.requests import get_user
from Keyboards.inline import profile_kb




async def profile_user(user_id: int, bot: Bot, message: Message):
    try:
        profile = await get_user(user_id)

        profile_text = (
    "┎🔍 <b>Профиль пользователя</b> 🔍\n"
    "┃\n"
    f"┣🎲 Звание: {profile.rank}"
    f"┣👤 Имя: <b>{profile.name}</b>\n"
    f"┣💰 Баланс: <b>{profile.balance}</b>\n"
    f"┣💎 Жизней осталось: <b>{profile.lives}</b>\n"
    "┃\n"
    "┣📅 Дата регистрации: ⬇\n"
    f"┣<b>{profile.registration_time}</b>\n"
    "┃\n"
    f"┣⚔️ Осталось ударов: <b>{profile.fuck}</b>\n"
    f"┣📥 Макс ударов: <b>{profile.fucked_up}</b>\n"
    "┃\n"
    "┣ <b>Закончились жизни и удары?\n"
    "┣ Жми кнопку ниже ⬇</b>\n"
    "┗━━━━━━━━━━━━━━━━━━━━━━━━━━"
)

        photos = await bot.get_user_profile_photos(user_id)
        
        if photos.photos:
            user_photo_path = photos.photos[0][-1].file_id
            await message.reply_photo(
                user_photo_path,
                caption=profile_text,
                parse_mode='html',
                reply_markup=profile_kb(user_id)
            )
        else:
            await message.reply(
                profile_text,
                parse_mode='html',
                reply_markup=profile_kb(user_id)
            )

    except Exception as e:
        print(f"Error in send_user_profile function: {e}")