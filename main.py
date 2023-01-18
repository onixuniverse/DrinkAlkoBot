import os
import logging

from aiogram import executor, Bot, Dispatcher
from dotenv import load_dotenv


def start(dp: Dispatcher):
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    load_dotenv()
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher(bot)

    from handlers import welcome_commands
    welcome_commands.register_handler(dp)

    start(dp)
