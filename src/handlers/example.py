from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("test"))
async def cmd_start(message: types.Message):
    await message.answer(str(message.chat.type))
