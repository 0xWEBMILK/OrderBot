from aiogram.fsm.state import StatesGroup, State

class DeleteOrder(StatesGroup):
    enter_target_id = State()