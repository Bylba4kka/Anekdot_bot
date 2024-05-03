import asyncio
import logging
import random

from handlers.interaction_handlers import reg_parser, comm
from settings import settings
from aiogram import Bot, Dispatcher


# Оповещение о запуске бота
async def start_up(bot: Bot):
    await comm(bot)
    await bot.send_message(chat_id=settings.bot.admin_id, text='Bot Started')


# Оповещение об отключении бота
async def shutdown(bot: Bot):
    await bot.send_message(chat_id=settings.bot.admin_id, text='Bot Shutdown')


# Регистрация обработчиков
def reg_handlers(dp: Dispatcher):
    reg_parser(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO
    )

    bot = Bot(settings.bot.bot_token, parse_mode="HTML")

    dp = Dispatcher()

    dp.startup.register(start_up)
    dp.shutdown.register(shutdown)

    reg_handlers(dp)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


# Точка запуска
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except(SystemExit, KeyboardInterrupt):
        print('Error')
