import json

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.callback_query_handler(text="add_channel")
async def add_channel(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer("Добавьте бота администратором в канал, затем перешлите любой пост из канала")
    await state.set_state("add_channel")


@dp.message_handler(state="add_channel")
async def add_channel_from_reply(message: types.Message, state: FSMContext):
    chat_id = message.forward_from_chat.id
    name = message.forward_from_chat.title
    username = message.forward_from_chat.username
    data = {
        f"{chat_id}": {
            "name": name,
            "username": username,
        }
    }

    with open("json/channel.json", "r") as f:
        jsn: dict = json.load(f)

    jsn.update(data)
    with open("json/channel.json", 'w') as f:
        json.dump(data, f)
    await dp.bot.send_message(chat_id=chat_id, text="Бот успешно добавлен в канал, данное сообщение можете удалить")
    await message.answer(f"Канал {name} успешно добавлен")
    await state.finish()
