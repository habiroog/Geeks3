from aiogram import types, Router
from aiogram.filters import Command

info_router = Router()

@info_router.message(Command('myinfo'))
async def info(message: types.Message):
    await message.answer(f'Ваш ID: {message.from_user.id}\n'
                         f'Ваше имя: {message.from_user.first_name}\n'
                         f'Ваше имя пользователя: {message.from_user.username}\n')
