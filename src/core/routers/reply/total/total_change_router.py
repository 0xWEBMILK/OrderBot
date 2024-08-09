from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.fsm import TotalCount
from core.utils.functions.total import append_total
from core.utils.config_reader import main_settings

router = Router()


file_path = main_settings.file_path.get_secret_value()
file_name = main_settings.file_name.get_secret_value()


@router.message(TotalCount.enter_total_count, F.text)
async def total_change(message: Message, state: FSMContext):
    try:
        total = int(message.text)
        await append_total(file_path, file_name, total)
        await message.answer('Кол-во обновлено!')
        await state.clear()
    except ValueError:
        await message.reply('Кол-во должно быть в виде числа!')