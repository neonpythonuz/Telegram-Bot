from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import base

menu = base.select_all_menu()

royhat = []
i = 0
for button in menu:
    if i == 0 or i != 1:
        royhat.append([KeyboardButton(text=button[1])])
    if i % 2 != 0:
        royhat.append([KeyboardButton(text=button[1])])
    i +=1

menu_buttons = ReplyKeyboardMarkup(keyboard=royhat,resize_keyboard=True)