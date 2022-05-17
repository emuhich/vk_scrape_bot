from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Группы"),
            KeyboardButton(text="Подробная информация"),

        ],
        [
            KeyboardButton(text="Все группы")

        ],
    ],

    resize_keyboard=True
)
