from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

router = Router()

@router.callback_query(StateFilter(None), F.data == "cancel")
async def cancel(callback: CallbackQuery, state: FSMContext):
    await callback.answer(text='Отменено!')
    await callback.message.delete()

    await state.clear()
