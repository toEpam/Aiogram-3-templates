from itertools import chain

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def book_keys_keyboard():
    keyboard = InlineKeyboardBuilder()
    buttons = [
        ["📍 Eng yaqin do'konni topish", "mylocation"],
        ["📱 Kontakt ulashish", "mycontact"],
    ]
    keyboard.row(*[InlineKeyboardButton(text=i[0], callback_data=i[1]) for i in chain(buttons)], width=1)
    return keyboard.as_markup()