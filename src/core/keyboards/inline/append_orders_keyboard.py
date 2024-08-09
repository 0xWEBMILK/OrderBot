from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def append_orders_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.add(InlineKeyboardButton(
        text="Отмена",
        callback_data="cancel")
    )

    builder.add(InlineKeyboardButton(
        text="Добавить заказы",
        callback_data="append_order")
    )

    builder.adjust(1)

    return builder