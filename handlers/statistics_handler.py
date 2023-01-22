from aiogram import Dispatcher
from aiogram.types import Message

from keyboards import general
from db import db


async def send_statistics(message: Message):
    statistics = await db.get_statistics(message.from_id)

    total_quantity = 0
    total_price = 0

    for elem in statistics:
        total_quantity += elem[0]
        total_price += elem[1]

    await message.reply(f"Ваша статистика за всё время\n\n"
                        f"Всего выпито алкоголя: {total_quantity} мл\n"
                        f"Всего выпито на: {total_price} рублей.", reply_markup=general.general_keyboard)


def register_handler(dp: Dispatcher):
    dp.register_message_handler(send_statistics, regexp="📊 Статистика")
