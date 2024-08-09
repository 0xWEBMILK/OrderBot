from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.fsm.AppendOrder import AppendOrder
from core.utils.functions.orders import append_order
from core.utils.functions.orders import remove_count
from core.utils.functions.total import fetch_total
from core.utils.config_reader import main_settings

router = Router()


file_path = main_settings.file_path.get_secret_value()
file_name = main_settings.file_name.get_secret_value()


@router.message(AppendOrder.enter_count, F.text)
async def enter_count(message: Message, state: FSMContext):
    total = await fetch_total(file_path, file_name)
    try:
        int(total)
        if int(total) < int(message.text):
            await message.answer('Недостаточно кол-ва на складе')

        else:
            data = await state.get_data()

            await message.answer('Данные обновлены!')

            await remove_count(file_path, file_name, message.text)
            await append_order(
                file_path,
                file_name,
                phone_number=data['phone_number'],
                count=message.text)

            await state.clear()
    except:
        await message.reply('Что-то пошло не так!')