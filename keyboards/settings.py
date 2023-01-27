from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# Settings Keyboard
settings_btn_1 = KeyboardButton("⛔ Danger Area")
settings_btn_2 = KeyboardButton("🔰 Главное меню")

settings_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
settings_keyboard.row(settings_btn_1, settings_btn_2)


# Danger Area Settings Keyboard
das_btn_1 = KeyboardButton("🗑 Удалить мою статистику")
das_btn_2 = KeyboardButton("🔰 Главное меню")

das_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
das_keyboard.add(das_btn_1).add(das_btn_2)
