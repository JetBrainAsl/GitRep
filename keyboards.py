from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

b1 = KeyboardButton("Night checklist")
b2 = KeyboardButton("Night report")
b3 = KeyboardButton("Daily and pocket reports")
b31 = KeyboardButton("Audit")
b30 = KeyboardButton("Назад")
b4 = KeyboardButton("Ночной админ")
b40 = KeyboardButton("Создание брони и заселение")
b5 = KeyboardButton("Дневной админ")
b6 = KeyboardButton("Профайлы")
b7 = KeyboardButton("Объяснительные")
b8 = KeyboardButton("Создать PM")
b9 = KeyboardButton("Продлить PM")

kb_night = ReplyKeyboardMarkup(resize_keyboard=True)
kb_welcome = ReplyKeyboardMarkup(resize_keyboard=True)
kb_day = ReplyKeyboardMarkup(resize_keyboard=True)

kb_night.add(b1).insert(b2).add(b3).insert(b31).add(b9).insert(b8).add(b30)
kb_welcome.add(b4).insert(b5).add(b6).insert(b7)
kb_day.add(b40).add(b30)
