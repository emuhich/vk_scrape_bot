from aiogram.dispatcher.filters import Command
from aiogram import types

from keyboards.default import menu
from loader import dp
from utils.misc.scrape import start


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Выберете пункт меню", reply_markup=menu)
    await start()
