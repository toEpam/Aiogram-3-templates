from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="start",
            description="Botni ishga tushurish",
        ),
        BotCommand(
            command="help",
            description="Yordam",
        ),
    ]

    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())
