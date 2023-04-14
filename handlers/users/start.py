from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from loader import dp,base, bot


from keyboards.default.menu import menu_buttuns
from keyboards.default.taomlar_uchun import taomlar_buttuns
from keyboards.default.ichimliklar_uchun import ichimliklar_buttuns
from keyboards.default.shirinliklar_uchun import shirinliklar_buttuns
from keyboards.default.fast_food_uchun import fast_food_buttuns
from keyboards.inline.tillar_uchun import tillar_buttuns

from keyboards.default.menu import menu_buttuns_eng
from keyboards.default.taomlar_uchun import dishes_buttuns
from keyboards.default.ichimliklar_uchun import drinks_buttuns
from keyboards.default.shirinliklar_uchun import dessert_buttuns
from keyboards.default.fast_food_uchun import fast_food_buttuns_eng

from filters.shaxsiy_uchun import Shaxsiy


@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    ismi = message.from_user.first_name
    familyasi = message.from_user.last_name
    usernamei = message.from_user.username
    user_id = message.from_user.id
    try:
        base.user_qoshish(ism=ismi, tg_id=user_id, fam=familyasi,username=usernamei)
    except Exception:
        pass
    await message.answer(f"Botga hush kelipsiz", reply_markup=tillar_buttuns)

@dp.message_handler(text = 'Taomlar')
async def bot_start(message: types.Message):
    await message.answer(f"Taomlar birini tanlang, {message.from_user.username}!", reply_markup=taomlar_buttuns)

@dp.callback_query_handler(text="til1")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Botga hush kelipsiz", reply_markup=menu_buttuns)

@dp.message_handler(text = 'Ichimliklar')
async def bot_start(message: types.Message):
    await message.answer(f"Ichimliklardan birini tanlang, {message.from_user.username}!", reply_markup=ichimliklar_buttuns)@dp.message_handler(text = 'Ichimliklar')

@dp.message_handler(text = "Shirinliklar")
async def bot_start(message: types.Message):
    await message.answer(f"Shirinliklardan birini tanlang, {message.from_user.username}!", reply_markup=shirinliklar_buttuns)

@dp.message_handler(text = "Fast food")
async def bot_start(message: types.Message):
    await message.answer(f"Fast foodlardan birini tanlang, {message.from_user.username}!", reply_markup=fast_food_buttuns)

@dp.message_handler(text = "Ortga")
async def bot_start(message: types.Message):
    await message.answer(f"Fast foodlardan birini tanlang, {message.from_user.username}!", reply_markup=menu_buttuns)

@dp.message_handler(text = "Back")
async def bot_start(message: types.Message):
    await message.answer(f"Welcome to the bot",  reply_markup=menu_buttuns_eng)

@dp.callback_query_handler(text="til2")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Welcome to the bot", reply_markup=menu_buttuns_eng)

@dp.message_handler(text="Dishes")
async def bot_start(message: types.Message):
    await message.answer(f"Choose one of the dishes", reply_markup=dishes_buttuns)

@dp.message_handler(text="Drinks")
async def bot_start(message: types.Message):
    await message.answer(f"Choose one of the drinks", reply_markup=drinks_buttuns)

@dp.message_handler(text="Desserts")
async def bot_start(message: types.Message):
    await message.answer(f"Choose one of the desserts", reply_markup=dessert_buttuns)

@dp.message_handler(text="Fast-food")
async def bot_start(message: types.Message):
    await message.answer(f"Choose one of the desserts", reply_markup=fast_food_buttuns_eng)

@dp.message_handler(commands="reklama", chat_id='789362160')
async def bot_start(message: types.Message):
    userlar = base.select_all_foydalanuvchilar()
    for user in userlar:
        await bot.send_message(chat_id=user[4], text="Bu reklaman")


@dp.message_handler(commands="foydalanuvchi")
async def bot_start(message: types.Message):
    userlar = base.select_foydalanuvchilar()
    print(userlar)




@dp.message_handler(commands="sanash", chat_id='789362160')
async def bot_start(message: types.Message):
    sanash = base.sanash_foydalanuvchilar()
    guruh_id = message.from_user.id
    for sana in sanash:
        await bot.send_message(chat_id=guruh_id, text=f"{sanash[0]} ta foydalanuvchi bor")