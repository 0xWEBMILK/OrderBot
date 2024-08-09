from aiogram import Router, F
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from core.fsm import TotalCount

router = Router()

@router.callback_query(StateFilter(None), F.data == "change_total")
async def change_total(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text='Введите допустимое кол-во!')
    
    await state.set_state(TotalCount.enter_total_count)
