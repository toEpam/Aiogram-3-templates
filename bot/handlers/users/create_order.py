from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, ShippingQuery, PreCheckoutQuery

from bot.data.config import ADMINS
from bot.data.products import python_book, ds_praktikum, FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING
from bot.keyboards.inline.product_keys import build_keyboard
from loader import bot

order_router = Router()
@order_router.message(Command("kitob"))
async def show_invoices(message: Message):
    caption = "<b>Pythonda Dasturlash Asoslari</b> kitobi.\n\n"
    caption += "Ushbu kitob bugungi kunda dasturlash asoslariga oid o’zbek tilidagi mukammal tuzilgan qo’llanmalardan biridir.\n\n"
    caption += "Qo’lingizdagi kitobning o’ziga xos jihati shundaki, uning har bir bo’limi uchun tayyorlangan qo'shimcha onlayn"
    caption += "materiallar, jumladan, 50 dan ortiq video darslar, amaliy mashg’ulotlar va vazifalarning kodlari e’tiboringizga havola etilgan.\n\n"
    caption += "O’quvchilar bu materiallarni maxsus QR kod yordamida o’z komputerlariga yuklab olib, ulardan unumli foydalanishi mumkin.\n\n"
    caption += "Narxi: <b>50000 so'm</b>"
    await message.answer_photo(photo="https://i.imgur.com/0IvPPun.jpg",
                         caption=caption, reply_markup=build_keyboard("book"))

@order_router.message(Command("praktikum"))
async def show_invoices(message: Message):
    caption = "<b>Data Science va Sun'iy Intellekt</b> praktikum.\n\n"
    caption += "6 oyda eng zamonaviy kasb egasi bo'ling.\n\n"
    caption += "Kurs tarkibi:\n"
    caption += "✅ Python Dasturlash Asoslar (4 hafta)\n"
    caption += "✅ Data Sciencega kirish va DS metodologiyasi (2 hafta)\n"
    caption += "✅ Maʻlumotlar tahlili (Data Analysis) (4 hafta)\n"
    caption += "✅ Maʻlumotlarga ishlov berish (4 hafta)\n"
    caption += "✅ Vizualizasiya (2 hafta)\n"
    caption += "✅ Machine Learning (6 hafta)\n"
    caption += "✅ Deep Learning (4 hafta)\n"
    caption += "✅ Natural Language Processing (4 hafta)\n\n"
    caption += "Narxi: <b>1.5mln so'm</b>"

    await message.answer_photo(photo="https://i.imgur.com/vRN7PBT.jpg",
                         caption=caption, reply_markup=build_keyboard("praktikum"))

@order_router.message(Command("mahsulotlar"))
async def book_invoice(message: Message):
    await bot.send_invoice(chat_id=message.from_user.id,
                           **python_book.generate_invoice(),
                           payload="123456")
    await bot.send_invoice(chat_id=message.from_user.id,
                           **ds_praktikum.generate_invoice(),
                           payload="123457")

@order_router.callback_query(lambda call: call.data == "product:book")
async def book_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **python_book.generate_invoice(),
                           payload="payload:kitob")
    await call.answer()


@order_router.callback_query(lambda call: call.data == "product:praktikum")
async def praktikum_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **ds_praktikum.generate_invoice(),
                           payload="payload:praktikum")
    await call.answer()


@order_router.shipping_query()
async def choose_shipping(query: ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Chet elga yetkazib bera olmaymiz")
    elif query.shipping_address.city.lower() == "tashkent":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
                                        ok=True)
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[REGULAR_SHIPPING],
                                        ok=True)


@order_router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Xaridingiz uchun rahmat!")
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"Quyidagi mahsulot sotildi: {pre_checkout_query.invoice_payload}\n"
                                f"ID: {pre_checkout_query.id}\n"
                                f"Telegram user: {pre_checkout_query.from_user.first_name}\n"                                
                                f"Xaridor: {pre_checkout_query.order_info.name}, tel: {pre_checkout_query.order_info.phone_number}")