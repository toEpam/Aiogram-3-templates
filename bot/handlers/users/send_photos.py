from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import InputFile, Message, FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

from loader import bot

media_router = Router()


@media_router.message(F.PHOTO)
async def get_file_id_p(message: Message):
    await message.reply(message.photo[-1].file_id)


@media_router.message(F.VIDEO)
async def get_file_id_v(message: Message):
    await message.reply(message.video.file_id)


@media_router.message(Command("kitob"))
async def send_book(message: Message):
    photo_id = "AgACAgUAAxkBAAIHUWErOgOL_YUiW1bawxdvEJM8mUd9AAK4rDEbXltZVRPBqDf39UdmAQADAgADeQADIAQ"
    photo_url = "https://kitoblardunyosi.uz/image/cache/catalog/001-Kitoblar/003_boshqalar/006_ilmiy_ommabop/python-3d-web-500x500h.jpg"
    # photo_file = InputFile(path_or_bytesio="/media/images/kitob.jpg")
    photo_file = FSInputFile(path="./media/images/kitob.jpg")
    await message.reply_photo(
        photo_file, caption="Dasturlash asoslari kitobi. \n Narxi: 50000 so'm"
    )
    await message.answer_photo(
        photo_id, caption="Dasturlash asoslari kitobi. \n Narxi: 50000 so'm"
    )
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo_url,
        caption="Dasturlash asoslari kitobi. \nNarxi: 50000 so'm",
    )


@media_router.message(Command("kurslar"))
async def send_courses(message: Message):
    media_group = MediaGroupBuilder()
    photo1 = "AgACAgUAAxkBAAIHa2ErPWwh50geLqoE4Hn5SGCdi09mAAK8rDEbXltZVUoM_yKC7xVRAQADAgADeQADIAQ"
    photo2 = "https://i0.wp.com/mohirdev.uz/wp-content/uploads/photo1627374915.jpeg"
    photo3 = "https://i1.wp.com/mohirdev.uz/wp-content/uploads/Telegram-bot.png"
    photo4 = InputFile(filename="/media/images/algoritm.png")
    video1 = "BAACAgUAAxkBAAIHT2ErOXldS7NxbW9mdL4tsI18ZqlvAALdAgACXltZVVoMJafxpb77IAQ"
    media_group.add_photo(photo1)
    media_group.add_photo(photo2)
    media_group.add_photo(photo3)
    media_group.add_photo(photo4)
    media_group.add_video(video=video1, caption="Bizning online kurslarimiz")
    await message.reply_media_group(media_group)
