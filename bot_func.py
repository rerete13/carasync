from aiogram import Bot
from aiogram.enums.chat_member_status import ChatMemberStatus
from tokens import Bot_token
from data_func import create_user_data, get_info_about
from btns import menu_keyboard_btn, inline_keyboard_url, inline_keyboard_call
from another_info import get_city_repaire
import datetime
import json

bot = Bot(Bot_token)


async def is_user_subscribed(message):

    chat_member = await bot.get_chat_member(chat_id='@autopars3', user_id=message.from_user.id)
    
    if str(chat_member.status.name) in ['CREATOR', 'ADMINISTRATOR', 'MEMBER']:
        return True
    else:
        return False



async def check_user_sub_status(msg):
    if await is_user_subscribed(msg) == True:
        await create_user_data(msg, 'user-data')
        return True
        
    else:
        await msg.answer("<b>Підпишися на канал:</b>🏎 @autopars3", reply_markup=inline_keyboard_url('🏎 @autopars3', 'https://t.me/autopars3'))
        return False
    
    
    
async def create_city_repaire_service_call(call, num:int):
    place, map = (await get_city_repaire(num))
    
    out = '' 
    for i in range(len(place)):
        x = place[i].split('\n')
        y = f'<a href="{map[i]}">{x[0]}</a>\n{x[1]}\n<code>{x[2]}</code>\n\n'
        
        out += y
        

    out += '\n\n Інформація надана від: @autoparse_bot'
    
    await call.bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text=out, reply_markup=inline_keyboard_call(text='Назад ⭕️', call='back'))


async def get_count_days(id):

    id = str(id)


    now = datetime.datetime.now()
    now = str(now.strftime("%d-%m-%Y %H:%M:%S"))

    get_time = (await get_info_about(f'user-data/{id}', 'info', 'bot-start'))

    now = datetime.datetime.strptime(now, '%d-%m-%Y %H:%M:%S')
    time_obj = datetime.datetime.strptime(get_time, '%d-%m-%Y %H:%M:%S')

    res = now - time_obj

    return res