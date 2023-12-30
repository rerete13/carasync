from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from another_info import repairs_and_citys



def back():
    return types.InlineKeyboardButton(text='Назад ⭕️', callback_data='back')


def inline_keyboard_url(text:str, link:str):
    btn = InlineKeyboardBuilder()
    btn.row(types.InlineKeyboardButton(text=text, url=link))
    
    return btn.as_markup()


def inline_keyboard_call(text:str, call:str):
    btn = InlineKeyboardBuilder()
    btn.row(types.InlineKeyboardButton(text=text, callback_data=call))
    
    return btn.as_markup()


def menu_keyboard_btn():
    btns = [
        [KeyboardButton(text='Меню')],
    ]
    
    btns = ReplyKeyboardMarkup(keyboard=btns)
    
    return btns


def inline_user_subscribe_start():
    btn = InlineKeyboardBuilder()
    btn.row(types.InlineKeyboardButton(text='🏎 autopars3', url='https://t.me/autopars3'))
    btn.row(types.InlineKeyboardButton(text='Вже підписався ✅', callback_data='sub_check'))

    return btn.as_markup()


def inline_menu_btn():
    btn = InlineKeyboardBuilder()
    btn.row(types.InlineKeyboardButton(text='Топ-10 найпопулярніших нових автомобілів у 2023', callback_data='top_car_10'))
    btn.row(types.InlineKeyboardButton(text='🛠 Автосервіси', callback_data='repairs'))
    # btn.row(types.InlineKeyboardButton(text='🔬 INFO', callback_data='info'))
    btn.row(types.InlineKeyboardButton(text='🍫 Власник', callback_data='owner'))
    btn.row(types.InlineKeyboardButton(text='🗣 Відгуки', callback_data='respons_3'))
    btn.row(types.InlineKeyboardButton(text='👤 Акаунт', callback_data='account'))

    return btn.as_markup()


def more_response_btn():
    btn = InlineKeyboardBuilder()
    btn.row(types.InlineKeyboardButton(text='🗣 Більше відгуків', callback_data='respons_9'))
    btn.row(back())

    return btn.as_markup()


def top_car_btn():
    btn = InlineKeyboardBuilder()
    btn.row(types.InlineKeyboardButton(text='🗣 Більше відгуків', callback_data='top_car_50'))
    btn.row(back())

    return btn.as_markup()


async def city_repaire_choose_btn():
    
    link, city = (await repairs_and_citys())
    
    btn = InlineKeyboardBuilder()
    btn.row(types.InlineKeyboardButton(text=city[0], callback_data='city_kyiv'))
    btn.row(types.InlineKeyboardButton(text=city[1], callback_data='city_kyivob'))
    btn.row(types.InlineKeyboardButton(text=city[2], callback_data='city_vinnycia'))
    btn.row(types.InlineKeyboardButton(text=city[4], callback_data='city_dnipro'))
    btn.row(types.InlineKeyboardButton(text=city[10], callback_data='city_frankivsk'))
    btn.row(types.InlineKeyboardButton(text=city[13], callback_data='city_lviv'))
    btn.row(types.InlineKeyboardButton(text=city[15], callback_data='city_odesa'))
    btn.row(types.InlineKeyboardButton(text=city[16], callback_data='city_poltava'))
    btn.row(types.InlineKeyboardButton(text=city[21], callback_data='city_kharkiv'))
    btn.row(types.InlineKeyboardButton(text=city[23], callback_data='city_hmelnyck'))
    btn.row(types.InlineKeyboardButton(text=city[24], callback_data='city_cherkasy'))
    btn.row(back())
    
    return btn.as_markup()



