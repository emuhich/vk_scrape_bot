import json

from aiogram import types

from keyboards.inline.callback_datas import set_callback, group_callback
from keyboards.inline.dinamic_keyboard import genmarkup, genmarkup_channel
from keyboards.inline.group_information import keyboard_group_info
from loader import dp


@dp.message_handler(text='Все группы')
async def show_menu_group(message: types.Message):
    with open("json/group.json", "r") as f:
        data: dict = json.load(f)
    list = [0, 9]
    await message.answer("Выберите нужную вам группу:", reply_markup=genmarkup(data, list))


@dp.callback_query_handler(set_callback.filter(text_name="forward"))
async def show_forward_group(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.delete()
    end = callback_data.get("end")
    with open("json/group.json", "r") as f:
        data: dict = json.load(f)
    list = [int(end), int(end) + 9]
    await call.message.answer("Выберите нужную вам группу:", reply_markup=genmarkup(data, list))


@dp.callback_query_handler(set_callback.filter(text_name="back"))
async def show_forward_group(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.delete()
    start = callback_data.get("start")
    with open("json/group.json", "r") as f:
        data: dict = json.load(f)
    list = [int(start) - 9, int(start)]
    await call.message.answer("Выберите нужную вам группу:", reply_markup=genmarkup(data, list))


@dp.callback_query_handler(set_callback.filter(text_name="forward_channel"))
async def show_forward_group(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.delete()
    end = callback_data.get("end")
    group_name = callback_data.get("group")
    with open("json/channel.json", "r") as f:
        data: dict = json.load(f)
    list = [int(end), int(end) + 9]
    await call.message.answer("Выберите нужную вам группу:", reply_markup=genmarkup_channel(data, list, group_name))


@dp.callback_query_handler(set_callback.filter(text_name="back_channel"))
async def show_forward_group(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.delete()
    start = callback_data.get("start")
    group_name = callback_data.get("group")
    with open("json/channel.json", "r") as f:
        data: dict = json.load(f)
    list = [int(start) - 9, int(start)]
    await call.message.answer("Выберите нужную вам группу:", reply_markup=genmarkup_channel(data, list, group_name))


@dp.callback_query_handler(group_callback.filter(text_name='group_info'))
async def show_forward_group(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.delete()
    group_name = callback_data.get("group")
    with open("json/channel.json", "r") as f:
        data: dict = json.load(f)
    list = [0, 9]
    await call.message.answer("Выберете канал который хотите добавить",
                              reply_markup=genmarkup_channel(data, list, group_name))


@dp.callback_query_handler(lambda call: call.data.split("|")[1] == 'group')
async def group_actions(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    group_name = call.data.split('|')[0]
    with open("json/group.json", "r") as f:
        data: dict = json.load(f)
    await call.message.answer(text=f"Вы выбрали группу: {group_name}", reply_markup=keyboard_group_info(group_name))


@dp.callback_query_handler(lambda call: call.data.split("|")[1] == 'channel')
async def group_actions(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    channel_id = call.data.split('|')[0]
    group_name = call.data.split('|')[2]
    with open("json/group.json", "r") as f:
        jsn: dict = json.load(f)
    list_channels = jsn[group_name]['channel']
    list_channels.append(channel_id)
    jsn[group_name].update({'channel': list(set(list_channels))})
    with open("json/group.json", 'w') as f:
        json.dump(jsn, f)
    await call.message.answer(f"Канал успешно добавлен в группу")