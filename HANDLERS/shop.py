from aiogram import types
from aiogram.types import InputFile

from loader import dp, bot
from image_creator import create_image
from parser_ import get_current_shop

from random import choice
from string import ascii_lowercase
from os import remove
from asyncio import sleep


@dp.message_handler(commands=["shop"])
async def start(message: types.Message):
    shop = get_current_shop()
    await message.answer("<b>Получил информацию из базы. Создаю изображения...</b>")

    images = [create_image(data) for name, data in shop.items()]

    media_group = types.MediaGroup()

    for i in range(1, len(images)):
        if i % 11 == 0:
            await message.answer_media_group(media_group)

            media_group = types.MediaGroup()

        filename = str(i)
        path = f"temp/{filename}.jpg"

        images[i].save(path)
        media_group.attach_photo(InputFile(path))

    await message.answer_media_group(media_group)
