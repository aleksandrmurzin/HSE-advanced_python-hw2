from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command

from src.utils.text import bq

router = Router()  # [1]


@router.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    welcome_message = f"""Здравствуйте {bq(message.from_user.username)}!
\nЭтот бот поможет Вам перевести текст с Русского на Английский!
\nДля того чтобы начать нажмите /translate и следуйте инструкции.
"""
    await message.answer(welcome_message, parse_mode=ParseMode.HTML)
