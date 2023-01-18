from aiogram import types, Dispatcher


async def send_welcome(message: types.Message):
    message = "Привет! Я бот для ведения статистики по количеству выпитого алкоголя.\n" \
              ""
    await message.reply("Привет!")


def register_handler(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
