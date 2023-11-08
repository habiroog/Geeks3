from aiogram import types, Router, F
from aiogram.filters import Command
from db.queries import get_all, get_by_category


faculties_router = Router()

@faculties_router.message(Command('faculties'))
async def faculties(message: types.Message):
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

@faculties_router.message(F.text.lower() == 'лингвистики')
async def show_linguistics(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    linguistics = get_by_category(1)
    await message.answer('Студенты факультета Лигвистики', reply_markup=kb)
    for student in linguistics:
        await message.answer(student[1])

@faculties_router.message(F.text.lower() == 'филологии')
async def show_philology(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    philology = get_by_category(2)
    await message.answer('Студенты факультета Филологии', reply_markup=kb)
    for student in philology:
        await message.answer(student[1])

@faculties_router.message(F.text.lower() == 'программирования')
async def show_programming(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    programming = get_by_category(3)
    await message.answer('Студенты факультета Программирования', reply_markup=kb)
    for student in programming:
        await message.answer(student[1])

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
