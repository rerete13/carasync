from aiogram import types, Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot_func import is_user_subscribed
from btns import menu_keyboard_btn, inline_user_subscribe_start, inline_menu_btn, inline_keyboard_call, more_response_btn, top_car_btn, city_repaire_choose_btn
from data_func import create_user_data
from another_info import all_comments, top_cars_sales

router = Router()


@router.callback_query(F.data == 'sub_check')
async def callback_return(callback: types.callback_query):
    if await is_user_subscribed(callback.message) == True:
        await callback.bot.delete_message(message_id=callback.message.message_id, chat_id=callback.message.chat.id)
        await create_user_data(callback.message, 'user-data')
        await callback.message.answer("<b>Введіть номер у такій формі:</b> AA7777AA", reply_markup=menu_keyboard_btn())
        
    else:
        await callback.message.answer("<b>Підпишися на канал:</b>🏎 @autopars3", reply_markup=inline_user_subscribe_start())





@router.callback_query(F.data.startswith("respons_"))
async def callbacks_num(callback: types.CallbackQuery):
    action = callback.data.split("_")[1]

    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text='⏳ Це може зайняти деякий час...')
    
    if action == "3":
        out = ''
        for i in range(3):
            # This comment clarifies that you are awaiting the all_comments(i) coroutine and then accessing the first element of the resulting list. It can serve as a helpful reminder for anyone reading the code, including yourself in the future, about the purpose of that specific line.
            out += (await all_comments(i))[0] + '\n\n'

        out += '\n\n Інформація надана від: @autoparse_bot'
            
        await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text=out, reply_markup=more_response_btn())

        
    if action == "9":
        out = ''
        for i in range(9):
            out += (await all_comments(i))[0] + '\n\n'

        out += '\n\n Інформація надана від: @autoparse_bot'
            
        await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text=out, reply_markup=inline_keyboard_call(text='Назад ⭕️', call='back'))



@router.callback_query(F.data.startswith("top_car_"))
async def callbacks_num(callback: types.CallbackQuery):
    action = callback.data.split("_")[2]

    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text='⏳ Це може зайняти деякий час...')
    
    if action == "10":
        out = ''
        info = (await top_cars_sales())
        for i in range(10):
            out += info[i] + '\n'

        out += '\n\n Інформація надана від: @autoparse_bot'
            
        await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text=out, reply_markup=top_car_btn())

        
    if action == "50":
        out = ''
        info = (await top_cars_sales())
        for i in range(50):
            out += info[i] + '\n'

        out += '\n\n Інформація надана від: @autoparse_bot'
            
        await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text=out, reply_markup=inline_keyboard_call(text='Назад ⭕️', call='back'))



@router.callback_query(F.data == 'repairs')
async def callback_return(callback: types.callback_query):
    await callback.message.answer('Виберіть місто', reply_markup= (await city_repaire_choose_btn()))
    



'city_kyiv'
'city_kyivob'
'city_vinnycia'
'city_dnipro'
'city_frankivsk'
'city_lviv'
'city_odesa'
'city_poltava'
'city_kharkiv'
'city_hmelnyck'
'city_cherkasy'


    


@router.callback_query(F.data == 'back')
async def callback_return(callback: types.callback_query):
    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text='Меню', reply_markup=inline_menu_btn())