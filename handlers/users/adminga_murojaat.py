from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.menu import tasdiqlash_buttuns, menu_buttuns

from loader import dp, bot

from filters.shaxsiy_uchun import Shaxsiy
from states.holatlar import Form
# Echo bot
@dp.message_handler(Shaxsiy(),text="Adminga murojaat")
async def bot_echo(message: types.Message):

    await message.answer(text="Ismni kiriting")
    await Form.ism_holati.set()

@dp.message_handler(Shaxsiy(),state=Form.ism_holati)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({"ismi": ism})
    await message.answer(text="Familya kiriting")
    await Form.fam_holati.set()

@dp.message_handler(Shaxsiy(),state=Form.fam_holati)
async def bot_echo(message: types.Message, state:FSMContext):
    familya = message.text
    await state.update_data({"fam": familya})
    await message.answer(text="Tel kiriting")
    await Form.tel_holati.set()

@dp.message_handler(Shaxsiy(),state=Form.tel_holati)
async def bot_echo(message: types.Message, state:FSMContext):
    nomer = message.text
    await state.update_data({"tel": nomer})
    await message.answer(text="Murojaat kiriting")
    await Form.murojaat_holati.set()

@dp.message_handler(Shaxsiy(),state=Form.murojaat_holati)
async def bot_echo(message: types.Message, state:FSMContext):
    matn = message.text
    await state.update_data({"text":matn})
    malumot = await state.get_data()
    ism = malumot.get("ismi")
    familya = malumot.get("fam")
    tel = malumot.get("tel")
    murojaat = malumot.get("text")

    text= f"Ism : {ism}\n" \
          f"Fam : {familya}" \
          f"Tel : {tel}" \
          f"Murojaat : {murojaat}"
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text=text, reply_markup=tasdiqlash_buttuns)
    await bot.send_message(chat_id=user_id, text="Ma'lumotlar to'g'rimi ? ", reply_markup=tasdiqlash_buttuns)

    await Form.tasdiqlash_holati.set()


@dp.message_handler(Shaxsiy(),state=Form.tasdiqlash_holati, text="Yo'q")
async def bot_echo(message: types.Message, state:FSMContext):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text="Bekor qilindi", reply_markup=menu_buttuns)
    await state.finish()

@dp.message_handler(Shaxsiy(),state=Form.tasdiqlash_holati, text="Ha")
async def bot_echo(message: types.Message, state:FSMContext):
    user_id = message.from_user.id
    malumot = await state.get_data()
    ism = malumot.get("ismi")
    familya = malumot.get("fam")
    tel = malumot.get("tel")
    murojaat = malumot.get("text")
    username = message.from_user.id

    text = f"Ism : {ism}\n" \
           f"Fam : {familya}\n" \
           f"Tel : {tel}\n" \
           f"Murojaat : {murojaat}\n" \
           f"Username : {username}"


    await bot.send_message(chat_id=789362160, text=text)
    await bot.send_message(chat_id=user_id, text="Adminga yuborildi", reply_markup=menu_buttuns)

    await state.finish()

