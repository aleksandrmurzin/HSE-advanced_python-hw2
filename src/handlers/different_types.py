from aiogram import F, Router
from aiogram.types import Message

from src.filters.chat_type import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter())


@router.message(F.sticker)
async def message_with_sticker(message: Message):
    await message.answer("Это стикер, но я не умею их переводить")


@router.message(F.animation)
async def message_with_gif(message: Message):
    await message.answer("А это GIF!, тоже ничего, но все не то.")
