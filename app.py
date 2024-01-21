import asyncio
import logging
import sys
from aiogram import Bot
from aiogram.enums import ParseMode
import handlers
from data.config import BOT_TOKEN
from loader import dp
from utils import on_startup_notify
from utils.set_bot_commands import set_default_commands
import betterlogging as bl
def setup_logging():
    """
    Set up logging configuration for the application.

    This method initializes the logging configuration for the application.
    It sets the log level to INFO and configures a basic colorized log for
    output. The log format includes the filename, line number, log level,
    timestamp, logger name, and log message.

    Returns:
        None

    Example usage:
        setup_logging()
    """
    log_level = logging.INFO
    bl.basic_colorized_config(level=log_level)

    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")


async def main() -> None:
    # setup_logging()

    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dp)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())