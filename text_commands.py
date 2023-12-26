import asyncio
from aiogram import types, F, Router, Bot
from aiogram.types import Message
from aiogram.filters import Command
from btns import inline_keyboard_call, menu_keyboard_btn, inline_menu_btn
from get_car_info import process_number
from bot_func import check_user_sub_status
from data_func import add_user_data
from tokens import Bot_token

bot = Bot(Bot_token)

router = Router()



@router.message(F.text == 'Меню')
async def menu(msg: Message):
    await msg.answer('Меню', reply_markup=inline_menu_btn())


@router.message(F.text)
async def menu(msg: Message):
    if await check_user_sub_status(msg) == False:
        return
    else:
        delete_message = await msg.answer(f'⏳ Це може зайняти деякий час...')
        
    number = msg.text.upper()
    
    await add_user_data(f'user-data/{msg.from_user.id}', 'findings', number, None)
    
    await process_number(bot, msg, number, delete_message)
    
    
    

    
    
    





