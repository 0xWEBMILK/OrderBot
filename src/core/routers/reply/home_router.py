from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

router = Router()

from core.keyboards.reply.home_keyboard import home_keyboard


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(message.text, reply_markup=home_keyboard())
    await state.clear()


@router.message(Command("help"))
async def cmd_help(message: Message, state: FSMContext):
    await message.answer(message.text, reply_markup=home_keyboard())
    await state.clear()