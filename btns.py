from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup




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


def languige_choose_btn():
    btn = InlineKeyboardBuilder()
    btn.row(types.InlineKeyboardButton(text='🇺🇦', callback_data='lan_ua'))
    btn.row(types.InlineKeyboardButton(text='🇷🇺', callback_data='lan_ru'))
    btn.row(types.InlineKeyboardButton(text='🇬🇧', callback_data='lan_en'))
    
    return btn.as_markup()




def inline_menu_btn():
    btn = InlineKeyboardBuilder()
    btn.row(types.InlineKeyboardButton(text='Топ-10 найпопулярніших нових автомобілів у 2023', callback_data='top10'))
    btn.row(types.InlineKeyboardButton(text='🛠 Автосервіси', callback_data='repairs'))
    btn.row(types.InlineKeyboardButton(text='🔬 INFO', callback_data='info'))
    btn.row(types.InlineKeyboardButton(text='🍫 Власник', callback_data='owner'))
    btn.row(types.InlineKeyboardButton(text='🗣 Відгуки', callback_data='respon'))
    btn.row(types.InlineKeyboardButton(text='👤 Акаунт', callback_data='account'))

    return btn.as_markup()

