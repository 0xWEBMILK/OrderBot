from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def total_count_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.add(InlineKeyboardButton(
        text="Отмена",
        callback_data="cancel")
    )

    builder.add(InlineKeyboardButton(
        text="Изменить данные",
        callback_data="change_total")
    )

    builder.adjust(1)

    return builder