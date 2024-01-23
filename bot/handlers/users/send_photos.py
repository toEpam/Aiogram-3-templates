from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import InputFile, Message, FSInputFile, InputMediaPhoto
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
    photo_url = "https://telegra.ph/file/fd053ddb8d0fbee95e85e.png"
    photo_file = FSInputFile(path="./media/images/kitob.jpg")
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo_url,
        caption="Dasturlash asoslari kitobi. \nNarxi: 50000 so'm",
    )
    await message.reply_photo(
        photo_file, caption="Dasturlash asoslari kitobi. \n Narxi: 50000 so'm"
    )


@media_router.message(Command("kurslar"))
async def send_courses(message: Message):
    media_group = MediaGroupBuilder()
    photo1 = "https://i1.wp.com/mohirdev.uz/wp-content/uploads/Telegram-bot.png"
    # photo2 = FSInputFile("/media/images/algoritm.png")
    photo3 = "AgACAgIAAxkBAAEYSIRlrlKZuq62fZDh5mc8w9oBP174egACSs8xG5FfeUkfo12lWIhSEAEAAwIAA3gAAzQE"
    video = "BQACAgIAAxkBAAEYSIllrlM_qgGdxLG8MGK5O9BbQ_DgUgAC4jwAApFfeUnQMpGuXu2X-DQE"
    # InputMediaPhoto(media=photo2)
    # media_group.add_photo(media=photo1)
    # media_group.add_photo(media=photo2)
    # media_group.add_video(media=video, caption="Bizning online kurslarimiz")

    media_group = MediaGroupBuilder(caption="Media group caption")

    # Add photo
    # media_group.add_photo(media=photo1)
    media_group.add(type="photo", media=photo1)
    # media_group.add_photo(media=photo2)
    # media_group.add_photo(media=photo3)
    # media_group.add(type="video", media=FSInputFile("/media/videos/video.webm"))
    await message.reply_media_group(media_group)
