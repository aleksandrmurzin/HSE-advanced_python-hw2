from aiogram import F, Router
from aiogram.types import Message

from bot.filters.chat_type import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter())

@router.message(~F.text)
async def process_non_text(message: Message) -> None:
    await message.answer("К сожалению, я полезен лишь при вызове команд, попробуте нажать /translate, чтобы сделать перевод.")

# @router.message(F.text)
# async def process_text(message: Message) -> None:
#     await message.answer("К сожалению, я полезен лишь при вызове команд, попробуте нажать /translate, чтобы сделать перевод.")
