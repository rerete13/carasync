import asyncio
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from btns import inline_keyboard_call, menu_keyboard_btn, inline_menu_btn
from get_car_info import creat_info

router = Router()



@router.message(F.text == 'Меню')
async def menu(msg: Message):
    await msg.answer('Меню', reply_markup=inline_menu_btn())


@router.message(F.text)
async def menu(msg: Message):

    await msg.answer('Меню')





