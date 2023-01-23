import re

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from db import db
from keyboards import alcohol, general


class FSMAddDrink(StatesGroup):
    tg_id = State()
    drink = State()
    date = State()
    quantity = State()
    price = State()


async def alcohol_start(message: types.Message):
    await FSMAddDrink.drink.set()

    await message.answer("🍸 Итак, какой напиток Вы выпили?", reply_markup=alcohol.drinks_keyboard)


async def cancel_alcohol_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer("❌ Добавление напитка отменено.", reply_markup=general.general_keyboard)


async def load_drink(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tg_id'] = message.from_id
        data['drink'] = message.text

    await FSMAddDrink.next()

    await message.reply("📅 Когда Вы его выпили?\nНажмите на кнопку или введите дату в формате ДЕНЬ.МЕСЯЦ.ГОД\n\n"
                        "При вводе некорректной даты, статистика может быть также некорректной.",
                        reply_markup=alcohol.dates_keyboard)


async def load_date(message: types.Message, state: FSMContext):
    if re.match(r"(0?[1-9]|[12][0-9]|3[01]).(0?[1-9]|1[012]).(2023)", message.text):
        async with state.proxy() as data:
            data['date'] = message.text

        await FSMAddDrink.next()

        await message.reply("🍷 Введите массу напитка в миллилитрах.", reply_markup=alcohol.quantity_keyboard)
    else:
        await message.reply("Введена некорректная дата!", reply_markup=alcohol.dates_keyboard)


async def load_quantity(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['quantity'] = message.text
        await FSMAddDrink.next()

        await message.reply("💸 Какая стоимость у напитка?", reply_markup=ReplyKeyboardRemove())
    else:
        await message.reply("Введена некорректная масса!", reply_markup=alcohol.quantity_keyboard)


async def load_price(message: types.Message, state: FSMContext):
    try:
        message.text = message.text.replace(",", ".")

        async with state.proxy() as data:
            data['price'] = float(message.text)

        await db.add_statistics(state)

        async with state.proxy() as data:
            await message.answer(f"✅ Отлично, напиток добавлен!\n\nНапиток: {data['drink']}\nДата: {data['date']}\n"
                                 f"Количество: {data['quantity']}мл\nЦена: {data['price']}",
                                 reply_markup=general.general_keyboard)

        await state.finish()
    except ValueError:
        await message.reply("Введена некорректная стоимость!", reply_markup=ReplyKeyboardRemove())


def register_handler(dp: Dispatcher):
    dp.register_message_handler(alcohol_start, regexp="🍸 Добавить напиток", state=None)
    dp.register_message_handler(cancel_alcohol_fsm, regexp="отмена", state="*")
    dp.register_message_handler(cancel_alcohol_fsm, Text(equals="отмена", ignore_case=True), state="*")
    dp.register_message_handler(load_drink, state=FSMAddDrink.drink)
    dp.register_message_handler(load_date, state=FSMAddDrink.date)
    dp.register_message_handler(load_quantity, state=FSMAddDrink.quantity)
    dp.register_message_handler(load_price, state=FSMAddDrink.price)
