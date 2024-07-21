#   ИМПОРТЫ
#-------------------------------------------------------------#
import datetime

from modules.Filters import Filter, IsAdmin
from aiogram.types import Message
from aiogram import F, Router, Bot
from aiogram.filters import CommandStart, Command
from message import (no_start_text, yes_start_text,
                      commands_text, reply_message,rank_text)
from Keyboards.inline import start_kb
from database.requests import (get_user,update_fuck,
                                select_user,  update_lives,
                                  update_rank_user, score_rang, edit_nic)
from datetime import datetime
from modules.check_group import is_reply_from_bot
from modules.profile import profile_user
#-------------------------------------------------------------#
#-------------------------------------------------------------#

router_admin = Router()

@router_admin.message(F.text.in_(["/админ", "/Адм", "/адм"]))
async def admin(message: Message, bot: Bot):
    ...

