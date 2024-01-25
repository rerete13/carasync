import asyncio
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from bot_func import check_user_sub_status
from btns import inline_keyboard_url, menu_keyboard_btn


router = Router()

@router.message(Command('start'))
async def start(msg: Message):
    if await check_user_sub_status(msg) == False:
        return False
    else:
        await msg.answer("<b>Введіть номер у такій формі:</b> AA7777AA", reply_markup=menu_keyboard_btn())
        
 

@router.message(Command('info'))
async def start(msg: Message):
    
    await msg.answer("<b>Bласник:</b> @rerete13\n\nНа їжу:\n<code>4441111132314539</code> \n\n<b>USDT (TRC20)</b> \n<code>TVSrox5rnjdK7Y2WL4dji3qyfb9yGb616f</code> \n\n <b>BTC (BTC)</b> \n<code>bc1qsmy29mvt4gmfuex8xscalvnu5vfg6hjaf796ph</code>")
    
    
    
# @router.message(Command('test'))
# async def start(msg: Message):
#     await msg.answer(str(msg))
    
    
    