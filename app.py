import asyncio

from aiogram import Bot
from aiogram.enums import ParseMode

from bot.data.config import BOT_TOKEN
from bot.handlers.logs.log_handler import setup_logging
from bot.handlers.users import routers_list
from bot.utils import on_startup_notify
from bot.utils.set_bot_commands import set_commands
from loader import dp
from bot.handlers import *

async def main() -> None:
    dp.include_routers(*routers_list)
    setup_logging()

    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)

    # Birlamchi komandalar (/star va /help)
    await set_commands(bot)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())