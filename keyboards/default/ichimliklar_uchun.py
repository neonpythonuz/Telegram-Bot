from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
ichimliklar_buttuns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Dena"),
            KeyboardButton(text="Cola"),
            KeyboardButton(text="Pepsi"),
            KeyboardButton(text="Ice Tea")
        ],
        [
            KeyboardButton(text="Ortga")
        ]
    ],
    resize_keyboard=True
)

drinks_buttuns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Dena"),
            KeyboardButton(text="Cola"),
            KeyboardButton(text="Pepsi"),
            KeyboardButton(text="Ice Tea")
        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)