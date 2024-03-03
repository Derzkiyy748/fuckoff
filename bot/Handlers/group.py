#   ИМПОРТЫ
#-------------------------------------------------------------#
import datetime
import config

from modules.Filters import Filter
from aiogram.types import Message
from aiogram import F, Router, Bot
from aiogram.filters import CommandStart, Command
from message import (no_start_text, yes_start_text,
                      commands_text, reply_message,rank_text, rate_text)
from Keyboards.inline import start_kb
from database.requests import (insert_user, get_user,update_fuck,
                                select_user,  update_lives,
                                  update_rank_user, score_rang, edit_nic,
                                  update_vip_coin, update_lives_ob, update_fuck_ob, get_set)
from datetime import datetime
from modules.check_group import is_reply_from_bot
from modules.profile import profile_user
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   СОЗДАНИЕ РОУТЕРА  
#-------------------------------------------------------------#
router = Router()
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   ОБРАБОТЧИК КОМАНДЫ СТАРТ
#-------------------------------------------------------------#
@router.message(CommandStart(), Filter(chat=["group", "private"]))
async def start(message: Message, bot: Bot):
    user_id = message.from_user.id
    user_data = {
        'nick': message.from_user.first_name,
        'vip_balance': 50,
        'registration_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    try:
        if not await get_user(user_id):
            await insert_user(user_id, user_data)
            await message.reply(no_start_text(), reply_markup=start_kb())
        else:
            await message.reply(yes_start_text(), reply_markup=start_kb())
        return

    except Exception as e:
        await message.reply(f"Произошла ошибка при регистрации: {e}")
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   ОБРАБОТЧИК СПИСКА УДАРА
#-------------------------------------------------------------#
@router.message(F.text.in_(['уебать', 'Уебать', 'Ебнуть', 'ебануть', 'Ебануть', 'ебнуть', 'fuck', 'е', 'Е']),
                Filter(chat=["group"]))
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
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   ОБРАБОТЧИК КОМАНДЫ ПОМОЩЬ
#-------------------------------------------------------------#
@router.message(Command("help"), Filter(chat=["group", "private"]))
async def help(message: Message) -> str:
    await message.reply(commands_text(), parse_mode='html')
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   ОБРАБОТЧИК КОМАНДЫ РАНК
#-------------------------------------------------------------#
@router.message(Command('rank'), Filter(chat=["group", "private"]))
async def rank(message: Message) -> str:
    user_id = message.from_user.id
    user = await select_user(user_id)
    await message.reply(rank_text(user.rank), parse_mode='html')


@router.message(Command('rate'), Filter(chat=["group", "private"]))
async def rank(message: Message) -> str:
    user_id = message.from_user.id
    set = await get_set()
    
    await message.reply(rate_text(set.rate_life, set.rate_fuck), parse_mode='html')
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   ОБРАБОТЧИК КОМАНДЫ ПРОФИЛЬ ДЛЯ ГРУПП
#-------------------------------------------------------------#
@router.message(F.text.in_(['п', 'профиль', 'Профиль', 'П']), Filter(chat=["group"]))
async def profile(message: Message, bot: Bot) -> str:
    user_id = message.from_user.id
    next_rank = await score_rang(user_id)
    profile = await profile_user(user_id, bot, message, int(next_rank))
    
    return profile
#-------------------------------------------------------------#
#-------------------------------------------------------------#




@router.message(F.text.startswith('+ник'))
async def edit_nickname(message: Message, bot: Bot):
    edit_nick = message.text
    new_nick = edit_nick[5:100]
    try:

        if len(new_nick) > 40:
            await message.reply(f'❌Больше 40 символов в нике - не поддерживается\nКоличество: {len(new_nick)}')

        else:
            user_id = message.from_user.id
            await message.reply(f'✅Вы успешно сменили ник! {new_nick}')
            await edit_nic(user_id, new_nick)
    except Exception as e:
        await message.reply(f"Произошла ошибка при регистрации: {e}")


@router.message(F.text.startswith('+обмен у'))
async def obmen_coin(message: Message, bot: Bot):
    user_id = message.from_user.id
    text = message.text[9:100].strip() 

    if not text:
        return await message.reply('❌Укажите количество vip_coin для обмена.')

    try:
        amount_to_exchange = int(text)
    except ValueError:
        return await message.reply('❌Неверный формат. Укажите количество vip_coin целым числом.')

    user = await select_user(user_id)

    if user.vip_balance < amount_to_exchange:
        return await message.reply('❌У вас недостаточно vip_coin для обмена на удары.')
    
    rate = await get_set()

    hits_granted = amount_to_exchange * rate.rate_fuck

    await update_fuck_ob(user_id, hits_granted)
    await update_vip_coin(user_id, amount_to_exchange)

    user = await select_user(user_id)

    await message.reply(f'✅Вы успешно обменяли {amount_to_exchange} vip_coin на {int(hits_granted)} удар(ов).\n'
                        f'Теперь у вас {user.fuck} удар(ов) и {user.vip_balance} vip_coin.')
    


@router.message(F.text.startswith('+обмен ж'))
async def obmen_coin(message: Message, bot: Bot):
    user_id = message.from_user.id
    text = message.text[9:100].strip() 

    if not text:
        return await message.reply('❌Укажите количество vip_coin для обмена на жизни.')

    try:
        amount_to_exchange = int(text)
    except ValueError:
        return await message.reply('❌Неверный формат. Укажите количество vip_coin целым числом.')

    user = await select_user(user_id)

    if user.vip_balance < amount_to_exchange:
        return await message.reply('❌У вас недостаточно vip_coin для обмена.')
    
    rate = await get_set()

    life_granted = amount_to_exchange * rate.rate_life

    await update_lives_ob(user_id, life_granted)
    await update_vip_coin(user_id, amount_to_exchange)

    user = await select_user(user_id)

    await message.reply(f'✅Вы успешно обменяли {amount_to_exchange} vip_coin на {int(life_granted)} жизнь(ей).\n'
                        f'Теперь у вас {user.lives} жизнь(ей) и {user.vip_balance} vip_coin.')

    
    




