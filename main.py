from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keyboards import kb_night, kb_welcome, kb_day

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать в бот-ассистент Novotel!',
                           reply_markup=kb_welcome)  # создал клаву главное меню


@dp.message_handler(text='Ночной админ')
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите интересующий пункт',
                           reply_markup=kb_night)  # создал клавиатуру ночного


@dp.message_handler(text='Дневной админ')
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите интересующий пункт',
                           reply_markup=kb_day)  # создал клавиатуру ночного


@dp.message_handler(text='Ночной чеклист')
async def process_help_command(message: types.Message):
    document = open("Files/Night Auditor.pdf", "rb")
    await bot.send_document(message.from_user.id, document=document)


@dp.message_handler(text='Создание брони')
async def process_help_command(message: types.Message):
    document = open("Files/Создание брони.pdf", "rb")
    await bot.send_document(message.from_user.id, document=document)


@dp.message_handler(text='Продлить PM')
async def process_help_command(message: types.Message):
    document = open("Files/Продлить PM.pdf", "rb")
    await bot.send_document(message.from_user.id, document=document)


@dp.message_handler(text='Создать PM')
async def process_help_command(message: types.Message):
    document = open("Files/Создать PM.pdf", "rb")
    await bot.send_document(message.from_user.id, document=document)


@dp.message_handler(text='Ночные отчеты')
async def process_help_command(message: types.Message):
    document = open("Files/Отчеты.pdf", "rb")
    await bot.send_document(message.from_user.id, document=document)


@dp.message_handler(text='Daily and pocket отчеты')
async def process_help_command(message: types.Message):
    document = open("Files/Daily, Pocket reports.pdf", "rb")
    await bot.send_document(message.from_user.id, document=document)


@dp.message_handler(text='Audit')
async def process_help_command(message: types.Message):
    document = open("Files/Аудит процесс.pdf", "rb")
    await bot.send_document(message.from_user.id, document=document)

@dp.message_handler(text='Постим начисления')
async def process_help_command(message: types.Message):
    document = open("Files/Постим.pdf", "rb")
    await bot.send_document(message.from_user.id, document=document)

@dp.message_handler(text='Заселение')
async def process_help_command(message: types.Message):
    document = open("Files/Заселение.pdf", "rb")
    await bot.send_document(message.from_user.id, document=document)

@dp.message_handler(text='Профайлы')
async def process_help_command(message: types.Message):
    document = open("Files/Профайлы + шеры.pdf", "rb")
    await bot.send_document(message.from_user.id, document=document)


@dp.message_handler(text=['Назад'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "_", reply_markup=kb_welcome)  # вернул на главное меню


if __name__ == '__main__':
    executor.start_polling(dp)
