from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

API_TOKEN: str = '6406018096:AAFOPLIfEXVlMDHr3p-1eZW9ROsUFcfqI-8'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')

async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')

async def send_echo(message: Message):
    await message.reply(text=message.text)

# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_help_command, Command(commands=['help']))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)