from aiogram import Bot
from aiogram.enums.chat_member_status import ChatMemberStatus
from tokens import Bot_token
from data_func import create_user_data
from btns import menu_keyboard_btn, inline_keyboard_url

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