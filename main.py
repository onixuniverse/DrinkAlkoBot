import os
import logging

from aiogram import executor, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv


def start(dp: Dispatcher):
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    load_dotenv()
    bot = Bot(token=os.getenv("TOKEN"))
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    from handlers import welcome_handler, alcohol_handler, statistics_handler
    welcome_handler.register_handler(dp)
    alcohol_handler.register_handler(dp)
    statistics_handler.register_handler(dp)

    start(dp)
