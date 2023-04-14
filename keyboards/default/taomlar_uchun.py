from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
taomlar_buttuns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Osh'),
            KeyboardButton(text="Sho'rva"),
            KeyboardButton(text='Mastava')
        ],
        [
            KeyboardButton(text='Shashlik'),
            KeyboardButton(text='Manti')
        ],
        [
            KeyboardButton(text="Ortga")
        ]
    ],
    resize_keyboard=True
)

dishes_buttuns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pilaf"),
            KeyboardButton(text="Soup"),
            KeyboardButton(text="Mastava")
        ],
        [
            KeyboardButton(text="Shashlik"),
            KeyboardButton(text="Manti")
        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)
