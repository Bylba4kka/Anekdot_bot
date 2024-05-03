from aiogram import Bot, Dispatcher, F, types
from aiogram.types import BotCommand, BotCommandScopeDefault, InputFile, CallbackQuery
from aiogram.filters import Command

from handlers.local_sessions import local_session
from keyboards.inline import keyboard, keyboard_for_ruslan
from parsing.berserk_parser import berserk_parser
from parsing.cool_stories_parser import cool_stories_parser
from parsing.jew_parser import jew_parser
from parsing.mem_2014_parser import mem_2014_parser
from parsing.stirlitz_parser import stirlitz_parser
from parsing.mem_for_ruslan import mem_for_ruslan_parser
from settings import settings


# Здесь в оперативной памяти хранятся шутки, которые были показаны уже
user_jokes = {}

# Здесь айдишники сообщений мемов, мемы берутся с приватного канала
random_mems_list = [102, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 193, 194]
meow_mems_list = [i for i in range(153, 191)]

# Парсинг сайтов с мемами при запуске бота. Все шутки хранятся в ОЗУ
stirlitz_list = stirlitz_parser()
jew_list = jew_parser()
cool_stories_list = cool_stories_parser()
mem_2014_list = mem_2014_parser()
mem_for_ruslan_list = mem_for_ruslan_parser()
berserk_list = berserk_parser()


# Команды бота
async def comm(bot: Bot):
    command = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
    ]
    await bot.set_my_commands(command, BotCommandScopeDefault())


# Обработчик команды /start
async def on_start(message: types.Message):
    # print(cool_stories_list)
    if message.chat.id == 2081304396:
        # Добавлена индивидуальная кнопка для друга Руслана
        await message.answer("Привет Руслан, нажми на кнопку чтобы получить анекдот", reply_markup=keyboard_for_ruslan)
    else:
        await message.answer("Привет, нажми на кнопку чтобы получить анекдот", reply_markup=keyboard)


# Обработчик команды 'Анекдот про Штирлица'
async def stirlitz(message: types.Message, bot: Bot):
    await local_session(stirlitz_list, user_jokes, message.from_user.id, 'stirlitz', message, bot)


# Обработчик команды 'Анекдот про Евреев'
async def jew(message: types.Message, bot: Bot):
    await local_session(jew_list, user_jokes, message.from_user.id, 'jew', message, bot)


# Обработчик команды 'мемы из 2014'
async def mem_2014(message: types.Message, bot: Bot):
    await local_session(mem_2014_list, user_jokes, message.from_user.id, 'mem_2014', message, bot)


# Обработчик команды 'интересные истории'
async def cool_stories(message: types.Message, bot: Bot):
    await local_session(cool_stories_list, user_jokes, message.from_user.id, 'cool_stories', message, bot)


# Обработчик команды "random meme"
async def random_meme(message: types.Message, bot: Bot):
    await local_session(random_mems_list, user_jokes, message.from_user.id,  'random_meme', message, bot)


# Обработчик команды 'meow meme'
async def meow_meme(message: types.Message, bot: Bot):
    await local_session(meow_mems_list, user_jokes, message.from_user.id, 'meow_meme', message, bot)


# Обработчик команды 'мем для руслана'
async def mem_for_ruslan(message: types.Message, bot: Bot):
    if message.chat.id == 2081304396:
        await local_session(mem_for_ruslan_list, user_jokes, message.from_user.id, 'mem_for_ruslan', message, bot)
    else:
        await message.reply("это мемы только для Руслана!")


# Обработчик команды 'berserk mem'
async def berserk_mem(message: types.Message, bot: Bot):
    await local_session(berserk_list, user_jokes, message.from_user.id, 'berserk_mem', message, bot)


# обработка сообщений пользователя
def reg_parser(dp: Dispatcher):
    dp.message.register(on_start, Command(commands='start'))
    dp.message.register(stirlitz, F.text == 'Анекдот про Штирлица')
    dp.message.register(jew, F.text == 'Анекдот про Евреев')
    dp.message.register(mem_2014, F.text == 'мемы из 2014')
    dp.message.register(cool_stories, F.text == 'интересные истории')
    dp.message.register(random_meme, F.text == 'random meme')
    dp.message.register(meow_meme, F.text == 'meow meme')
    dp.message.register(mem_for_ruslan, F.text == 'мем для руслана')
    dp.message.register(berserk_mem, F.text == 'berserk mem')
