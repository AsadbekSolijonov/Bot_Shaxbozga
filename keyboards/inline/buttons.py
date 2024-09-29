from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

in_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🇺🇿 uz', callback_data='uz'),
     InlineKeyboardButton(text='🇷🇺 ru', callback_data='ru'),
     ],
    [InlineKeyboardButton(text='🇺🇸 en', callback_data='en'),]
])
