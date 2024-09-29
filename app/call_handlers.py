from aiogram import Router, F
from aiogram.types import CallbackQuery

from utils.read_message import read

call_rt = Router()


@call_rt.callback_query(lambda callback: callback.data in ['uz', 'ru', 'en'])
async def uz(call: CallbackQuery):
    from utils.db.my_db import update
    chat_id = call.message.chat.id

    update(chat_id=chat_id, set_lang=call.data)
    datas = read(call.data)
    await call.message.answer(datas['select_lang'])
