import asyncio

from aiogram import Bot
from aiogram.enums import ParseMode

from bot.data import BOT_TOKEN
from bot.handlers import setup_logging
from loader import dp
from bot.utils import on_startup_notify
from bot.utils.set_bot_commands import set_commands


async def main() -> None:
    setup_logging()

    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)

    # Birlamchi komandalar (/star va /help)
    await set_commands(bot)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
