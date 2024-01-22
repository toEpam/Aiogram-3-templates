from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from bot.keyboards.default.contact_button import contact_keyboard

contact_router = Router()


@contact_router.callback_query(lambda call: call.data == "mycontact")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text="Kontakt yuboring:", reply_markup=contact_keyboard())

@contact_router.message(F.contact)
async def get_contact(message: Message):
    contact = message.contact
    await message.answer(f"Rahmat, <b>{contact.full_name}</b>.\n"
                         f"Sizning {contact.phone_number} raqamingizni qabul qildik.\nAdminmiz siz bilan bog'lanadi.",
                         reply_markup=ReplyKeyboardRemove())