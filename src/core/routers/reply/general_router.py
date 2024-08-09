from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(F.text.lower() == "отмена")
async def cancel(message: Message, state: FSMContext):
    await message.answer("Ваше состояние сброшено!")
    await state.clear()