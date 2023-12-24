from aiogram import types, Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot_func import is_user_subscribed
from btns import menu_keyboard_btn, inline_user_subscribe_start
from data_func import create_user_data

router = Router()


@router.callback_query(F.data == 'sub_check')
async def callback_return(callback: types.callback_query):
    if await is_user_subscribed(callback.message) == True:
        await callback.bot.delete_message(message_id=callback.message.message_id, chat_id=callback.message.chat.id)
        await create_user_data(callback.message, 'user-data')
        await callback.message.answer("<b>Введіть номер у такій формі:</b> AA7777AA", reply_markup=menu_keyboard_btn())
        
    else:
        await callback.message.answer("<b>Підпишися на канал:</b>🏎 @autopars3", reply_markup=inline_user_subscribe_start())
