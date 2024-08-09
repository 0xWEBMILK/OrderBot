from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.fsm.AppendOrder import AppendOrder
from core.utils.functions.orders.delete_order import delete_order
from core.utils.config_reader import main_settings

router = Router()


file_path = main_settings.file_path.get_secret_value()
file_name = main_settings.file_name.get_secret_value()


@router.message(AppendOrder.enter_phone_number, F.text)
async def enter_number(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text.lower())
    await message.answer(text="Введите кол-во")
    await state.set_state(AppendOrder.enter_count)