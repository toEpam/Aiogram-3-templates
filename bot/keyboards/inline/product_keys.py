from itertools import chain

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def build_keyboard(product):
    keyboard = InlineKeyboardBuilder()
    buttons = [
        ["Xarid qilish"]
    ]
    keyboard.row(*[InlineKeyboardButton(text=i, callback_data=f"product:{product}") for i in chain(*buttons)])
    return keyboard.as_markup()
