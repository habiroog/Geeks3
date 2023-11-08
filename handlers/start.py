from aiogram import types, Router, F
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command('start'))
async def start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='О нас')],
            [types.KeyboardButton(text='Адресс')],
            [types.KeyboardButton(text='Помощь')],
        ]
    )
    await message.answer(f'Привет, {message.from_user.first_name}!')
    await message.answer("Главное меню:", reply_markup=kb)
