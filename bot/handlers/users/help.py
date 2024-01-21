from aiogram import types
from aiogram.filters import Command

from bot.handlers.users.start import command_router


@command_router.message(Command('help'))
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))
