import json

from aiogram import types

from loader import dp


@dp.message_handler(text="Подробная информация")
async def show_menu_group_1(message: types.Message):
    with open("json/group.json", "r") as f:
        jsng = json.load(f)
    with open("json/channel.json", "r") as f:
        jsnc = json.load(f)
    await message.answer(f"Количество групп: {len(jsng)}\n"
                         f"Количество каналов: {len(jsnc)}\n")
