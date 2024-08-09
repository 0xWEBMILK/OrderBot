from aiogram.fsm.state import StatesGroup, State

class AppendOrder(StatesGroup):
    enter_phone_number = State()
    enter_count = State()