from aiogram import types

from loader import dp, bot
from aiogram.types import ContentType, InputFile

# Echo bot
@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()
    await message.answer(text="Dokument qabul qilindi")

@dp.message_handler(content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[1].download()
    await message.answer(text="Rasm qabul qilindi")

@dp.message_handler(content_types=ContentType.VIDEO)
async def bot_echo(message: types.Message):
    await message.video.download()
    await message.answer(text="Video qabul qilindi")

@dp.message_handler(text="Pilaf")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/315'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption="Cost --- 48 mig")

@dp.message_handler(text="Soup")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/317'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili, caption="Cost --- 45 ming")

@dp.message_handler(text="Mastava")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/313'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili, caption="Cost --- 40ming")

@dp.message_handler(text="Shashlik")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/316'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili, caption="Cost --- 21 ming")

@dp.message_handler(text="Manti")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/312'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili, caption="Cost --- 15 ming")

#Drinks


@dp.message_handler(text="Dena")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/319'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Cost --- 16  ming')

@dp.message_handler(text="Cola")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/322'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Cost --- 9  ming')

@dp.message_handler(text="Pepsi")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/321'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Cost --- 9  ming')

@dp.message_handler(text="Ice Tea")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/325'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Cost --- 6 ming')

#Disserts

@dp.message_handler(text="Ice cream")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/327'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Cost ---  10 ming')

@dp.message_handler(text="Carrot Cake")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/328'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Cost ---  18 ming')

@dp.message_handler(text="Apple Pie")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/329'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Cost ---  17 ming')

@dp.message_handler(text="Fudge")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/330'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Cost ---  22 ming')

@dp.message_handler(text="Chocolate Brownie")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/331'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Cost ---  16 ming')


#Fast food

@dp.message_handler(text="Hod-dog")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/332'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Cost ---  16 ming')

@dp.message_handler(text="Burger")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/333'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Cost ---  18 ming')

@dp.message_handler(text="Lavash")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/334'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Cost ---  25 ming')
