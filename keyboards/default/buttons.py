from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from utils.read_message import read


def default_btns(lang):
    datas = read(lang)

    btn = ReplyKeyboardMarkup(keyboard=[

        [KeyboardButton(text=datas['buttons']['share_contact'], request_contact=True),
         KeyboardButton(text=datas['buttons']['share_location'], request_location=True)],

        [KeyboardButton(text='⚙️ Sozlamalar'),
         KeyboardButton(text='🗣 Til o`zgartirish'),
         KeyboardButton(text='👩‍👩‍👧 Biz haqimizda')]

    ], resize_keyboard=True, one_time_keyboard=True)

    return btn
