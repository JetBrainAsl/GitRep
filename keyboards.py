from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

b1 = KeyboardButton("Ночной чеклист")
b2 = KeyboardButton("Ночные отчеты")
b3 = KeyboardButton("Daily and pocket отчеты")
b31 = KeyboardButton("Audit")
b30 = KeyboardButton("Назад")
b4 = KeyboardButton("Ночной админ")
b40 = KeyboardButton("Создание брони")
b5 = KeyboardButton("Дневной админ")
b6 = KeyboardButton("Профайлы")
b7 = KeyboardButton("Объяснительные")
b8 = KeyboardButton("Создать PM")
b9 = KeyboardButton("Продлить PM")
b10 = KeyboardButton("Заселение")
b11 = KeyboardButton("Постим начисления")

kb_night = ReplyKeyboardMarkup(resize_keyboard=True)
kb_welcome = ReplyKeyboardMarkup(resize_keyboard=True)
kb_day = ReplyKeyboardMarkup(resize_keyboard=True)

kb_night.add(b1).insert(b2).add(b3).insert(b31).add(b9).insert(b8).add(b10).insert(b11).add(b30)
kb_welcome.add(b4).insert(b5).add(b6).insert(b7)
kb_day.add(b40).add(b30)
