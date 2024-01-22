from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.states.personalData import PersonalData

state_router = Router()


# /form komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, None
@state_router.message(Command("form"))
async def enter_test(message: Message, state: FSMContext):
    await message.answer("To'liq ismingizni kiriting")
    await state.set_state(PersonalData.fullName)


@state_router.message(PersonalData.fullName)
async def answer_fullname(message: Message, state: FSMContext):
    fullname = message.text

    data = await state.get_data()
    data["fullname"] = fullname
    await state.set_data(data)

    await message.answer("Email manzil kiriting")

    await state.set_state(PersonalData.email)

@state_router.message(PersonalData.email)
async def answer_email(message: Message, state: FSMContext):
    email = message.text

    data = await state.get_data()
    data["email"] = email
    await state.set_data(data)

    await message.answer("Telefon raqam kiriting")

    await state.set_state(PersonalData.phoneNum)


@state_router.message(PersonalData.phoneNum)
async def answer_phone(message: Message, state: FSMContext):
    phone = message.text

    data = await state.get_data()
    data["phone"] = phone
    await state.set_data(data)
    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    msg = "Quyidai ma`lumotlar qabul qilindi:\n"
    msg += f"Ismingiz - {name}\n"
    msg += f"Email - {email}\n"
    msg += f"Telefon: - {phone}"
    await message.answer(msg)

    # State dan chiqaramiz
    # 1-variant
    await state.clear()

    # 2-variant
    # await state.reset_state()
    # Aiogramning 3-nchi versiyasida ishlamaydi!

    # 3-variant. Ma`lumotlarni saqlab qolgan holda
    # await state.reset_state(with_data=False)
    # Aiogramning 3-nchi versiyasida ishlamaydi!
