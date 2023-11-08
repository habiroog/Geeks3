from aiogram import types, Router
from aiogram.filters import Command

img_router = Router()


@img_router.message(Command('image'))
async def image(message: types.Message):
    file = types.FSInputFile('image/galaxy.jpg')
    await message.answer_photo(file)
