from aiogram import Router, F
from aiogram.types import Message
from aiogram.enums.parse_mode import *


router = Router()

from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from core.utils.config_reader import main_settings

from core.keyboards.inline.total_count_keyboard import total_count_keyboard
from core.keyboards.inline.get_orders_keyboard import get_orders_keyboard
from core.keyboards.inline.append_orders_keyboard import append_orders_keyboard

from core.utils.functions.total import fetch_total, fetch_temp
from core.utils.functions.orders import get_orders


file_path = main_settings.file_path.get_secret_value()
file_name = main_settings.file_name.get_secret_value()


@router.message(F.text.lower() == 'добавить данные', StateFilter(None))
async def append_data(message: Message):
    await message.answer("Добавить данные", reply_markup=append_orders_keyboard().as_markup())


@router.message(F.text.lower() == 'текущие данные', StateFilter(None))
async def current_data(message: Message):
    try:
        result = await get_orders(file_path, file_name)
        await message.answer(
            text=f"```Данные\n{result}```",
            parse_mode='Markdown',
            reply_markup=get_orders_keyboard().as_markup())
        
    except ValueError:
        await message.reply('Текущие данные не доступны')


@router.message(F.text.lower() == 'кол-во на складе', StateFilter(None))
async def total_count(message: Message, state: FSMContext):
    result = await fetch_temp(file_path, file_name)

    await message.answer(
            text=f"Кол-во на складе: {result}",
            reply_markup=total_count_keyboard().as_markup()
        )