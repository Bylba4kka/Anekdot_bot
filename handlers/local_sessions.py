import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile, URLInputFile

from keyboards.inline import keyboard


async def local_session(jokes, user_jokes, user_id, flag, message: Message, bot: Bot):
    user_id = str(user_id) + flag
    # Проверяем, есть ли пользователь в словаре
    if user_id not in user_jokes:
        user_jokes[user_id] = jokes.copy()

    if flag in ('random_meme', 'meow_meme') and user_jokes[user_id]:
        joke = random.choice(user_jokes[user_id])
        await bot.copy_message(message.from_user.id, -1001898519544, joke)
        user_jokes[user_id].remove(joke)

    elif user_jokes[user_id] and flag  in ('stirlitz', 'jew', 'cool_stories', 'mem_for_ruslan'):

        # Отправляем случайный анекдот пользователю
        joke = random.choice(user_jokes[user_id])
        await message.answer(joke)

        # Удаляем отправленный анекдот из списка для пользователя
        user_jokes[user_id].remove(joke)

    elif user_jokes[user_id] and flag in ('mem_2014', 'berserk_mem'):
        img_url = random.choice(user_jokes[user_id])

        image = URLInputFile(
            img_url,
            filename=img_url + flag
        )


        await bot.send_photo(message.chat.id, image)

        user_jokes[user_id].remove(img_url)
    else:
        await message.reply("Все анекдоты закончились. Запускаю по новой",
                            )
        del user_jokes[user_id]

