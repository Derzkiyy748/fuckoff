from aiogram.types import Message, CallbackQuery
from aiogram import F, filters, Router, Bot
from aiogram.filters import CommandStart
from message import start_text
from Keyboards.inline import start_kb

router = Router()
router.message.filter(F.chat.type == "group")



@router.message(CommandStart())
async def start(message: Message, bot: Bot):
    await message.reply(start_text(), reply_markup=start_kb())


@router.message(F.text == "уебать")
async def fuck(message: Message, bot: Bot):
    reply = message.reply_to_message
    if not reply:
        return await message.answer('уебок ты')
    await message.reply('Ты уебал уебка!')
