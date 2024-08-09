import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from core.fsm.AppendOrder import AppendOrder

router = Router()

@router.callback_query(StateFilter(None), F.data == "append_order")
async def append_order(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text='Введите номер телефона')
    await state.set_state(AppendOrder.enter_phone_number)
