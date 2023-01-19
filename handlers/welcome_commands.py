from aiogram import types, Dispatcher

from keyboards import general


async def send_welcome(message: types.Message):
    text = "Привет! Я бот для ведения статистики по количеству выпитого алкоголя.\n"
    await message.answer(text, reply_markup=general.general_keyboard)


def register_handler(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
