import sqlite3
from db.save import createtable
from aiogram import types, Router, F
from aiogram.filters import Command

subscribe_router = Router()

@subscribe_router.message(Command('subscribe'))
async def subscribe(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='Подписаться')],
        ],
        resize_keyboard=True
    )
    await message.answer('Подпишитесь, для получения новостей!', reply_markup=kb)

@subscribe_router.message(F.text.lower() == 'подписаться')
async def subscribe_(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    createtable()
    categoryId = message.chat.id
    user_id = message.chat.id
    user_name = message.chat.username
    conn = sqlite3.connect('db.users')
    c = conn.cursor()
    c.execute('''INSERT INTO users VALUES (?, ?, ?)''', (categoryId, user_id, user_name))
    conn.commit()
    conn.close()
    await message.answer('Спасибо за подписку!', reply_markup=kb)



