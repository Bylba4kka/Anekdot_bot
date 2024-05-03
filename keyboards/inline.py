from aiogram.types import BotCommand, BotCommandScopeDefault, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, \
    ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


keyboard = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder='перед использованием обновите, нажав /start',
    keyboard=[
        [
            KeyboardButton(text='Анекдот про Штирлица'),
            KeyboardButton(text='Анекдот про Евреев'),
        ],
        [
            KeyboardButton(text='мемы из 2014'),
            # KeyboardButton(text='интересные истории'),
        ],
        [
            KeyboardButton(text='random meme'),
            KeyboardButton(text='meow meme'),
        ],
        [
            KeyboardButton(text='berserk mem'),
        ]
    ]
)


keyboard_for_ruslan = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder='перед использование обновите, нажав /start',
    keyboard=[
        [
            KeyboardButton(text='Анекдот про Штирлица'),
            KeyboardButton(text='Анекдот про Евреев'),
        ],
        [
            KeyboardButton(text='мемы из 2014'),
            KeyboardButton(text='интересные истории'),
        ],
        [
            KeyboardButton(text='random meme'),
            KeyboardButton(text='meow meme'),
        ],
        [
            KeyboardButton(text='berserk mem'),
        ],
        [
            KeyboardButton(text='мем для руслана'),
        ],
    ]
)