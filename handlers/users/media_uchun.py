from aiogram import types


from loader import dp, bot
from aiogram.types import ContentType, InputFile, ReplyKeyboardRemove

from filters.shaxsiy_uchun import Shaxsiy

# Echo bot
# @dp.message_handler(content_types=ContentType.DOCUMENT)        #50mb  documentlarda oshmasligi kere
# async def bot_echo(message: types.Message):
#     await message.document.download()
#     await message.answer(text="Documant qabul qilindi")
#
# @dp.message_handler(content_types=ContentType.VIDEO)          #20 mb oshiq bo'lsa qabul qilmedi   bot oziga qabul qila oladi
# async def bot_echo(message: types.Message):
#     await message.video.download()
#     await message.answer(text="Video qabul qilindi")
#
# @dp.message_handler(content_types=ContentType.PHOTO)
# async def bot_echo(message: types.Message):
#     await message.photo[10].download()
#     await message.answer(text="Rasm qabul qilindi")

@dp.message_handler(Shaxsiy(),text="Osh")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/315'
    await bot.send_photo(chat_id= user_id,photo=rasm_manzili, caption='Narxi --- 48 ming')

    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="Sho'rva")
async def bot_echo(message : types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/317'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Narxi --- 45  ming')
    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="Mastava")
async def bot_echo(message : types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/313'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Narxi --- 40  ming')
    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="Shashlik")
async def bot_echo(message : types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/316'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Narxi --- 21  ming')
    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="Manti")
async def bot_echo(message : types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/312'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Narxi --- 15  ming')
    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())


# Drinks

@dp.message_handler(text="Dena")
async def bot_echo(message : types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/319'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Narxi --- 16  ming')
    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="Cola")
async def bot_echo(message : types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/322'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Narxi --- 9  ming')
    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="Pepsi")
async def bot_echo(message : types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/321'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Narxi --- 9  ming')
    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="Ice Tea")
async def bot_echo(message : types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/325'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Narxi --- 6 ming')
    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())

#Shirinliklar

@dp.message_handler(text="Muzqaymoq")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/327'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Narxi ---  10 ming')
    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Carrot Pirogi")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/328'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Narxi ---  18 ming')
    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Olmali Pirog")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/329'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Narxi ---  17 ming')
    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Fudge")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/330'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Narxi ---  22 ming')
    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Shokoladli Brownie")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/331'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Narxi ---  16 ming')
    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())

#Fast food

@dp.message_handler(text="Hod-dog")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/335'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Narxi ---  16 ming')
    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="Burger")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/333'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Narxi ---  18 ming')
    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="Lavash")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/textdoofine/334'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption='Narxi ---  25 ming')
    await bot.send_message(chat_id=user_id, text="Buyurtma tez orada qabul qilinadi, iltimos javob kelishini kuting :)", reply_markup=ReplyKeyboardRemove())

