import json

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.choice_buttom import choice
from loader import dp


@dp.message_handler(text='Группы')
async def show_menu_group(message: types.Message):
    await message.answer("Текущие группы:", reply_markup=choice)


@dp.callback_query_handler(text='add_new_group')
async def add_new_group(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer("Вставьте ссылку группы вк которую вы хотите добавить")
    await state.set_state("add_group")


@dp.message_handler(state="add_group")
async def add_group_json(message: types.Message, state: FSMContext):
    try:
        group_name = message.text.split('/')[3]
        data = {
            f"{group_name}": {
                "count_posts": 0,
                "offset": 0,
                "channel": [],
                "id": []
            }
        }

        with open("json/group.json", "r") as f:
            jsn: dict = json.load(f)
        if jsn.get(group_name):
            await message.answer(f"Группа {group_name}, была добавлена ранее")
        else:
            jsn.update(data)
            with open("json/group.json", 'w') as f:
                json.dump(jsn, f)
            await message.answer(f"Группа {group_name} успешно добавлена")
    except IndexError:
        await message.answer("Ввдеите коррекнтую ссылку группы пример: https://vk.com/nrnews24",
                             disable_web_page_preview=True)
    await state.finish()
