from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from datetime import datetime

from db import db


# Drinks Keyboard
drink_types = db.get_drink_types()
drinks_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

index = 0
while index < len(drink_types):
    try:
        drinks_keyboard.row(KeyboardButton(drink_types[index]), KeyboardButton(drink_types[index+1]))
        index += 2
    except IndexError:
        drinks_keyboard.add(KeyboardButton(drink_types[index]))
        index += 1


# Dates Keyboard
dates_btn = datetime.today().strftime('%d.%m.%Y')
dates_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
dates_keyboard.add(dates_btn)


# Count of drink Keyboard
count_btn_1 = KeyboardButton("50")
count_btn_2 = KeyboardButton("250")
count_btn_3 = KeyboardButton("500")
count_btn_4 = KeyboardButton("1000")
quantity_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
quantity_keyboard.row(count_btn_1, count_btn_2).row(count_btn_3, count_btn_4)
