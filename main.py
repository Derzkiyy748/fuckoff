import aiogram
import config
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from Handlers.group import router
from Handlers.callback_start import call_router
from database.models import asyn_main



async def main() -> None:
    await asyn_main()
    bot = Bot(config.TOKEN)
    dp = Dispatcher()
    dp.include_routers(router, call_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")