from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
fast_food_buttuns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Hod-dog'),
            KeyboardButton(text='Burger'),
            KeyboardButton(text='Lavash')
        ],
        [
            KeyboardButton(text="Ortga")
        ]
    ],
    resize_keyboard=True
)

fast_food_buttuns_eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Hod-dog'),
            KeyboardButton(text='Burger'),
            KeyboardButton(text='Lavash')
        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)