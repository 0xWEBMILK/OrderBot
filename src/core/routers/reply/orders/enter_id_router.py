from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.fsm.DeleteOrder import DeleteOrder
from core.utils.functions.orders.delete_order import delete_order
from core.utils.config_reader import main_settings

router = Router()


file_path = main_settings.file_path.get_secret_value()
file_name = main_settings.file_name.get_secret_value()


@router.message(DeleteOrder.enter_target_id, F.text)
async def enter_id(message: Message, state: FSMContext):
    try:
        ids = message.text
        await delete_order(file_path, file_name, ids)
        await message.answer('Заказы обновлены!')
        await state.clear()
    except ValueError:
        await message.reply('Произошёл сбой!')