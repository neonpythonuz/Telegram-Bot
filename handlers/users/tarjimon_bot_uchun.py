from aiogram import types
from googletrans import Translator
from loader import dp
tarjimon = Translator()

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    til = tarjimon.detect(text=message.text).lang
    if til == 'uz':
        tarjima_qilsh_en = tarjimon.translate(text=message.text, dest='en', src='uz').text
        await message.answer(text=f"{tarjima_qilsh_en}")
    elif til == 'en':
        tarjima_qilsh_en = tarjimon.translate(text=message.text, dest='uz', src='en').text
        await message.answer(text=f"{tarjima_qilsh_en}")
    elif til == 'ru':
        tarjima_qilsh_en = tarjimon.translate(text=message.text, dest='uz', src='ru').text
        await message.answer(text=f"{tarjima_qilsh_en}")
