import asyncio
from aiogram.types import BotCommand
from logging import basicConfig
from bot import dp, bot
from handlers import (
start_router,
info_router,
img_router,
faculties_router,
questions_router
)
async def main():
    await bot.set_my_commands(
        [
           BotCommand(command='start', description='Запустить бота'),
           BotCommand(command='image', description='Отправить картинку'),
           BotCommand(command='myinfo', description='Показать данные'),
           BotCommand(command='faculties', description='Открыть факультеты'),
            BotCommand(command='questions', description='Начать опрос')
        ]
    )

    dp.include_router(img_router)
    dp.include_router(info_router)
    dp.include_router(start_router)
    dp.include_router(faculties_router)
    dp.include_router(questions_router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    basicConfig(level='INFO')
    asyncio.run(main())
