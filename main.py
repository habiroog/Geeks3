import asyncio
from aiogram.types import BotCommand
from aiogram import Dispatcher
from logging import basicConfig
from bot import dp, bot, scheduler
from handlers import (
start_router,
info_router,
img_router,
faculties_router,
questions_router,
scheduler_router,
subscribe_router
)
from db.save import initdb, createtable
from db.queries import init_db, create_table, populate_tables


async def on_startup(dispatcher):
    print('Бот запущен')
    initdb()
    createtable()
    init_db()
    create_table()
    # populate_tables()
    scheduler.add_job()


async def main():
    await bot.set_my_commands(
        [
           BotCommand(command='start', description='Запустить бота'),
           BotCommand(command='image', description='Отправить картинку'),
           BotCommand(command='myinfo', description='Показать данные'),
           BotCommand(command='faculties', description='Открыть факультеты'),
           BotCommand(command='questions', description='Начать опрос'),
           BotCommand(command='remind', description='Напоминалка')
        ]
    )

    dp.startup.register(on_startup)

    dp.include_router(img_router)
    dp.include_router(info_router)
    dp.include_router(start_router)
    dp.include_router(faculties_router)
    dp.include_router(questions_router)
    dp.include_router(scheduler_router)
    dp.include_router(subscribe_router)

    scheduler.start()

    await dp.start_polling(bot)


if __name__ == '__main__':
    basicConfig(level='INFO')
    asyncio.run(main())


