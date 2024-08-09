from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_orders_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.add(InlineKeyboardButton(
        text="Отмена",
        callback_data="cancel")
    )

    builder.add(InlineKeyboardButton(
        text="Удалить заказ",
        callback_data="delete_order")
    )

    builder.adjust(1)

    return builder