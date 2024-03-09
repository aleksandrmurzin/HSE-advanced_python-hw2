from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_github_url_kb() -> types.InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(
        types.InlineKeyboardButton(
            text="GitHub",
            url="https://github.com/aleksandrmurzin/HSE-advanced_python-hw2",
        )
    )
    return kb.as_markup()


def get_rating_kb() -> types.InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for i in range(1, 6):
        kb.add(
            types.InlineKeyboardButton(text=str(i), callback_data=str(i) + "_rating")
        )
    return kb.as_markup()
