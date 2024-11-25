import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import TOKEN
from app.hendlers import router
from app.open import routerl
from app.rstart import rstartr, async_main


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    await async_main()
    dp.include_router(rstartr)
    dp.include_router(router)
    dp.include_router(routerl) 
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')