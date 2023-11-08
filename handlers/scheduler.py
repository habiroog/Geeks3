from aiogram import types, Router
from aiogram.filters import Command
from bot import bot, scheduler
from datetime import datetime

scheduler_router = Router()

@scheduler_router.message(Command('remind'))
async def remind_me(message: types.Message):
    user_id = str(message.chat.id)
    if scheduler.get_job(user_id) is not None:
        await message.answer('Вы уже нажимали!')
    else:
        scheduler.add_job(
            send_reminder,
            'cron',
            day_of_week="tue,wed,fri",
            hour="08",
            minute="30",
            id=user_id,
            kwargs={'chat_id': message.chat.id},
        )
        await message.answer('Понял, принял!')


async def send_reminder(chat_id: int):
    await bot.send_message(
        chat_id=chat_id,
        text='Бодрое утро!'
    )