from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_buttuns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Taomlar'),
            KeyboardButton(text='Ichimliklar')
        ],
        [
            KeyboardButton(text='Shirinliklar'),
            KeyboardButton(text='Fast food')

        ],
        [
            KeyboardButton(text="Adminga murojaat")
        ]

    ],

    resize_keyboard=True
)

menu_buttuns_eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Dishes'),
            KeyboardButton(text='Drinks')
        ],
        [
            KeyboardButton(text='Desserts'),
            KeyboardButton(text='Fast-food')

        ],

    ],
    resize_keyboard=True
)

tasdiqlash_buttuns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ha'),
            KeyboardButton(text="Yo'q")
        ],

    ],

    resize_keyboard=True
)
