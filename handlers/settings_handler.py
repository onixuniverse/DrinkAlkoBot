from aiogram import Dispatcher
from aiogram.types import Message

from keyboards import settings


async def send_settings(message: Message):
    await message.answer("Настройки", reply_markup=settings.settings_keyboard)


async def send_danger_area_settings(message: Message):
    await message.answer("⛔ Danger Area\n\nБудьте внимательны при выборе действия.", reply_markup=settings.das_keyboard)


async def delete_user_statistics(message: Message):
    await message.answer("Функция не доступна.", reply_markup=settings.das_keyboard)


def register_handler(dp: Dispatcher):
    dp.register_message_handler(send_settings, regexp="⚙ Настройки")
    dp.register_message_handler(send_danger_area_settings, regexp="⛔ Danger Area")
    dp.register_message_handler(delete_user_statistics, regexp="🗑 Удалить мою статистику")
