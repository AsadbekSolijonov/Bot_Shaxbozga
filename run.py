import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6874056136:AAHLp-QMOV6qu2z3Yf-CZ7YOG6FHhe5b2J4"
dp = Dispatcher()


async def main() -> None:
    from app.handlers import router
    from app.f_filters import rt
    from app.call_handlers import call_rt

    dp.include_routers(router, rt, call_rt)

    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
