from aiogram.dispatcher.filters.state import State, StatesGroup

class Form(StatesGroup):
    ism_holati = State()
    fam_holati = State()
    tel_holati = State()
    murojaat_holati = State()
    tasdiqlash_holati = State()