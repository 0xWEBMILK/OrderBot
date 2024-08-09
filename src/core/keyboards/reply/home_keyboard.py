from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def home_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    
    kb.button(text="Добавить данные")
    kb.button(text="Текущие данные")
    kb.button(text="Кол-во на складе")
    kb.adjust(2)

    return kb.as_markup(resize_keyboard=True)