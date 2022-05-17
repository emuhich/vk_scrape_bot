import math

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import set_callback


def genmarkup(data: dict, list):
    keyboard_markup = InlineKeyboardMarkup(row_width=3)
    row_btns = []
    count = 0
    start, end = list[0], list[1]
    data_list = [*data]
    count_list = len(data_list) / 9
    for group in data_list[start:end]:
        if count == 3:
            keyboard_markup.row(*row_btns)
            row_btns = []
            count = 0
        row_btns.append(InlineKeyboardButton(group, callback_data=f"{group}|group"))
        count += 1
    keyboard_markup.row(*row_btns)
    if len(data_list[end:]) <= 0:
        end -= 9
    if len(data_list[:start]) <= 0:
        start += 9
    keyboard_markup.add(
        InlineKeyboardButton('◀️',
                             callback_data=set_callback.new(start=start, end=end, text_name="back", group_name='1')),
        InlineKeyboardButton(f'{int(list[1] / 9)}/{math.ceil(count_list)}',
                             callback_data=set_callback.new(start=0, end=0, text_name="forward", group_name='1')),
        InlineKeyboardButton('▶️', callback_data=set_callback.new(start=start, end=end, text_name="forward",
                                                                  group_name='1')),
    )
    return keyboard_markup


def genmarkup_channel(data: dict, list, group):
    keyboard_markup = InlineKeyboardMarkup(row_width=3)
    row_btns = []
    count = 0
    start, end = list[0], list[1]
    data_list = [*data]
    count_list = len(data_list) / 9
    for channel in data_list[start:end]:
        if count == 3:
            keyboard_markup.row(*row_btns)
            row_btns = []
            count = 0
        row_btns.append(InlineKeyboardButton(data[channel]['name'], callback_data=f"{channel}|channel|{group}"))
        count += 1
    keyboard_markup.row(*row_btns)
    if len(data_list[end:]) <= 0:
        end -= 9
    if len(data_list[:start]) <= 0:
        start += 9
    keyboard_markup.add(
        InlineKeyboardButton('◀️', callback_data=set_callback.new(start=start, end=end, text_name="back_channel",
                                                                  group_name=group)),
        InlineKeyboardButton(f'{int(list[1] / 9)}/{math.ceil(count_list)}',
                             callback_data=set_callback.new(start=0, end=0, text_name="forward_channel",
                                                            group_name=group)),
        InlineKeyboardButton('▶️', callback_data=set_callback.new(start=start, end=end, text_name="forward_channel",
                                                                  group_name=group)),
    )
    return keyboard_markup
