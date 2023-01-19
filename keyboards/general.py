from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


button_1 = KeyboardButton("🍸 Добавить напиток")
button_2 = KeyboardButton("📊 Статистика")
button_3 = KeyboardButton("⚙ Настройки")

general_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
general_keyboard.add(button_1).row(button_2, button_3)
