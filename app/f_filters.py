from aiogram import F, Router
from aiogram.types import Message
from keyboards.inline.buttons import in_btn

rt = Router()


@rt.message(F.text == '⚙️ Sozlamalar')
async def setting(message: Message):
    await message.answer('Sozlamalar bo`limiga xush kelibsiz!')


@rt.message(F.text == '🗣 Til o`zgartirish')
async def setting(message: Message):
    await message.answer('Tilni tanlang!', reply_markup=in_btn)


@rt.message(F.text == '👩‍👩‍👧 Biz haqimizda')
async def setting(message: Message):
    await message.answer('Biz haqimizda ma`lumot')


@rt.message(F.text)
async def all_text_handler(message: Message):
    contact = message.text
    import re  # regular expression
    pattern = r"\+998(\s?\(\d{2}\)\s?\d{3}\s?\d{2}\s?\d{2}|\d{9})"
    if re.fullmatch(pattern, contact):
        await message.reply("Siz telefon raqam yubordingiz!")
    else:
        await message.reply("Bu telefon raqam emas!")


@rt.message(F.text)
async def calculate(message: Message):
    try:
        res = eval(message.text)
    except Exception as e:
        res = f"{e}"
    await message.reply(f"{res}")


@rt.message(F.photo)
async def photo_handler(message: Message):
    await message.answer('Siz rasm yubordingiz.')
    await message.answer(
        f'<a href="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRXqO4pBeLoXaegT8aDlnPzNBT0j-EmFaYi9_iL_ZFCago1SNWD"> CR7</a>')


@rt.message(F.document)
async def document_handler(message: Message):
    await message.answer('Siz document fayl yubordingiz!')
    await message.send_copy(chat_id=message.chat.id)


@rt.message(F.location)
async def location_handler(message: Message):
    await message.answer('Siz lokatsiya yubordingiz!')
    await message.send_copy(chat_id=message.chat.id)


@rt.message(F.contact)
async def contact_handler(message: Message):
    await message.answer('Siz kontakt yuboringiz!')
    await message.send_copy(chat_id=message.chat.id)
