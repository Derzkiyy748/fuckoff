#   МОДУЛИ
#-------------------------------------------------------------#
import config
import asyncio
import logging
import sys

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
    await asyn_main()
    bot = Bot(config.TOKEN)
    dp = Dispatcher()
    dp.include_routers(router, router_private, call_router)

    asyncio.create_task(system_rate(bot))

    await dp.start_polling(bot)
    print("Bot started")

#-------------------------------------------------------------#
#-------------------------------------------------------------#
    
    
#   ИНИЦИАЛИЗАЦИЯ БОТА
#-------------------------------------------------------------#
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
#-------------------------------------------------------------#
#-------------------------------------------------------------#