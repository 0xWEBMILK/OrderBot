import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from core.fsm.DeleteOrder import DeleteOrder

router = Router()

@router.callback_query(StateFilter(None), F.data == "delete_order")
async def delete_order(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Введите номер заказа')
    await state.set_state(DeleteOrder.enter_target_id)

    await asyncio.sleep(10)
    await callback.message.delete()
