import datetime

from modules.Filters import Filter
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router, Bot
from aiogram.filters import CommandStart, Command
from message import (no_start_text, yes_start_text,
                      commands_text, reply_message,
                        trigger, rank_text)
from Keyboards.inline import start_kb
from database.requests import (registration_user, get_user,update_fuck,
                                select_user,  update_lives,
                                  update_rank_user, score_rang)
from datetime import datetime
from modules.check_group import is_reply_from_bot
from modules.profile import profile_user


router = Router()



@router.message(CommandStart(), Filter(chat=["group", "private"]))
async def start(message: Message, bot: Bot):
    user_id = message.from_user.id
    user_data = {
        'name': message.from_user.full_name,
        'balance': 50,
        'registration_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    try:
        if not await get_user(user_id):
            await registration_user(user_id, user_data)
            await message.reply(no_start_text(), reply_markup=start_kb())
        else:
            await message.reply(yes_start_text(), reply_markup=start_kb())
        return

    except Exception as e:
        await message.reply(f"Произошла ошибка при регистрации: {e}")



@router.message(F.text.in_(trigger), Filter(chat=["group"]))
async def fuck(message: Message, bot: Bot):
    user_id = message.from_user.id
    reply = message.reply_to_message
    if not reply:
        return await message.reply('Вы должны ответить на сообщение вашего обитчика!')

    opponent_name = reply.from_user.first_name
    opponent_id = reply.from_user.id
    opponent_username = reply.from_user.username
    selected_user = await select_user(user_id)
    opponent = await select_user(opponent_id)

    if await is_reply_from_bot(message):
        return await message.reply('Я выше всех вас, балбесы. Я вне игры) 😎')
    elif opponent_id == user_id:
        return await message.reply('Вы не можете уебать самого себя. Не пытайся наебать меня! 😡')
    elif opponent is None:
        return await message.reply('Уебок не зарегистрирован в нашем боте, позови его и уеби чмоню! 😡')
    elif selected_user.fuck <= 0:
        return await message.reply('У вас недостаточно ударов, откисай 😢')
    elif opponent.lives <= 0:
        return await message.reply('У противника недостаточно жизней, увы..😢')
    elif selected_user.lives <= 0:
        return await message.reply('😢Для игры нужно иметь больше 1 жизни!\nПолучить жизни вы можете у себя в профиле\nКоманда "профиль","п"')
    
    await update_fuck(user_id, 1)
    selected_user = await select_user(user_id)
    await update_lives(opponent_id, 1)
    opponent = await select_user(opponent_id)

     # Проверяем, достиг ли пользователь нового ранга после каждого удара
    result = await update_rank_user(user_id)
    if result[0] == True:
        # Получаем текущий ранг после обновления
        await message.reply(f"🎉 Поздравляю! Вы достигли нового ранга: {result[1]}! 🎉\n"
                            f"Осталось {result[2]} ударов до следующего ранга.", parse_mode='html')
        
        await message.reply(reply_message(opponent_name, opponent_username, selected_user, opponent, result[2]), parse_mode='html')
    else:
        await message.reply(reply_message(opponent_name, opponent_username, selected_user, opponent, result[2]), parse_mode='html')



@router.message(Command("help"), Filter(chat=["group", "private"]))
async def help(message: Message) -> str:
    await message.reply(commands_text(), parse_mode='html')



@router.message(Command('rank'), Filter(chat=["group", "private"]))
async def rank(message: Message) -> str:
    user_id = message.from_user.id
    user = await select_user(user_id)
    await message.reply(rank_text(user.rank), parse_mode='html')



@router.message(F.text.in_(['п', 'профиль', 'Профиль', 'П']), Filter(chat=["group"]))
async def profile(message: Message, bot: Bot) -> str:
    user_id = message.from_user.id
    next_rank = await score_rang(user_id)
    profile = await profile_user(user_id, bot, message, int(next_rank))
    
    return profile
