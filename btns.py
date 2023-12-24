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
        [KeyboardButton(text='Маню')],
    ]
    
    btns = ReplyKeyboardMarkup(keyboard=btns)
    
    return btns




def languige_choose_btn():
    btn = InlineKeyboardBuilder()
    btn.row(types.InlineKeyboardButton(text='🇺🇦', callback_data='lan_ua'))
    btn.row(types.InlineKeyboardButton(text='🇷🇺', callback_data='lan_ru'))
    btn.row(types.InlineKeyboardButton(text='🇬🇧', callback_data='lan_en'))
    
    return btn.as_markup()

