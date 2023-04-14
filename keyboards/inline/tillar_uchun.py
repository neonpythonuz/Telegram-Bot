from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


tillar_buttuns = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek tili🇺🇿", callback_data="til1"),
            InlineKeyboardButton(text="Inglis tili🇬🇧", callback_data="til2")
        ],
        [
            InlineKeyboardButton(text="Hamkorlarimiz", url="https://t.me/ttylblog"),
            InlineKeyboardButton(text="Ulashish", switch_inline_query="botga a'zo boling")
        ]
    ]
)