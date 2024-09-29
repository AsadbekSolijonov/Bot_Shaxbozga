from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, ReplyKeyboardRemove
from aiogram import html, Router

from keyboards.default.buttons import default_btns
from utils.read_message import read

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    from utils.db.my_db import select
    from utils.db.my_db import insert

    chat_id = message.chat.id
    username = message.from_user.username
    default_lang = message.from_user.language_code

    try:
        insert(chat_id, username, default_lang)
    except Exception:
        pass

    lang = select(chat_id)
    datas = read(lang)

    await message.answer(f"{datas['start']}", reply_markup=default_btns(lang))


@router.message(Command('get_photo'))
async def send_img(message: Message):
    img = FSInputFile('media/cr71.png')
    await message.answer_photo(photo=img, caption='OK')


@router.message(Command('remove_btn'))
async def rmv_btn(message: Message):
    await message.reply("Oddiy tugmalar olib tashlandi", reply_markup=ReplyKeyboardRemove())
