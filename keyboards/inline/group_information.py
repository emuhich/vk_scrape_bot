from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import group_callback


def keyboard_group_info(group):
    information_keyboard = InlineKeyboardMarkup(row_width=2,
                                                inline_keyboard=[
                                                    [

                                                        InlineKeyboardButton(
                                                            text="Добавить канал",
                                                            callback_data=group_callback.new(text_name='group_info', group=group)

                                                        ),

                                                        InlineKeyboardButton(
                                                            text="Удалить канал",
                                                            callback_data="buy:apple:5"

                                                        )

                                                    ],

                                                ])
    return information_keyboard
