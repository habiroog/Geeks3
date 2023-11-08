from aiogram import types, Router, F
from aiogram.filters import Command


faculties_router = Router()

@faculties_router.message(Command('faculties'))
async def shop(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='Лингвистики')],
            [types.KeyboardButton(text='Филологии')],
            [types.KeyboardButton(text='Программирования')],
            [types.KeyboardButton(text='В начало')],
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите факультет ниже:", reply_markup=kb)

@faculties_router.message(F.text.lower() == 'Лингвистики')
async def show_books(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Кафедры факультета Лигвистики', reply_markup=kb)

@faculties_router.message(F.text.lower() == 'Филологии')
async def show_figurines(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Кафедры факультета Филологии', reply_markup=kb)

@faculties_router.message(F.text.lower() == 'Программирования')
async def show_accessories(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Кафедры факультета Программирования', reply_markup=kb)

@faculties_router.message(F.text.lower() == 'в начало')
async def inline(message: types.Message):
    await message.answer('Главное меню')
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(
                text='O нас', callback_data='aboutus')
            ],
            [types.InlineKeyboardButton(
                text='Наш инстаграмм', url='http://instagram.com')
            ],
        ]
    )
    await message.answer('Главное меню', reply_markup=kb)
