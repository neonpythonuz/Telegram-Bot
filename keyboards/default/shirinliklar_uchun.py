from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
shirinliklar_buttuns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Muzqaymoq"),
            KeyboardButton(text="Carrot Pirogi")
        ],
        [
            KeyboardButton(text="Olmali Pirog"),
            KeyboardButton(text="Fudge"),
            KeyboardButton(text="Shokoladli Brownie")
        ],
        [
            KeyboardButton(text="Ortga")
        ]
    ],
    resize_keyboard=True
)

dessert_buttuns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ice Cream"),
            KeyboardButton(text="Carrot Cake")
        ],
        [
            KeyboardButton(text="Apple Pie"),
            KeyboardButton(text="Fudge"),
            KeyboardButton(text="Chocolate Brownie")
        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)