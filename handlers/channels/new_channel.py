from aiogram import types
from loader import dp


@dp.message_handler(text="Привет")
async def add_new_channel(message: types.Message):
    await print(message)


@dp.message_handler(content_types=["new_chat_members"])
async def add_new_channel(message: types.Message):
    await print(message)
