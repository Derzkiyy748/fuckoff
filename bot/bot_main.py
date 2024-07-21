#   МОДУЛИ
#-------------------------------------------------------------#
import config
import asyncio
import logging
import sys
import tqdm
import time

from art import tprint
from aiogram import Bot, Dispatcher
from Handlers.group import router
from Handlers.private import router_private
from Handlers.callback_start import call_router
from database.models import asyn_main
from modules.system_Rate import system_rate

#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   ФУНКЦИЯ ЗАПУСКА
#-------------------------------------------------------------#
async def main():

    for _ in tqdm.tqdm(range(100)):
        time.sleep(0.02)
    tprint("Bot >>> started")

    await asyn_main()
    bot = Bot(config.TOKEN)
    dp = Dispatcher()
    dp.include_routers(router, router_private, call_router)

    asyncio.create_task(system_rate(bot))

    for i in config.ADMIN_ID:
        bot.send_message(i, "Bot started")

    await dp.start_polling(bot)


#-------------------------------------------------------------#
#-------------------------------------------------------------#
    
    
#   ИНИЦИАЛИЗАЦИЯ БОТА
#-------------------------------------------------------------#
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        tprint("Exit")
#-------------------------------------------------------------#
#-------------------------------------------------------------#
        