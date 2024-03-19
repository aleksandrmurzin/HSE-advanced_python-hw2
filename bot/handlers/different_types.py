from aiogram import F, Router
from aiogram.types import Message

from bot.filters.chat_type import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter())


@router.message(F.sticker)
async def message_with_sticker(message: Message):
    """
    :param message: message
    """
    await message.answer("Это стикер, но я не умею их переводить")


@router.message(F.animation)
async def message_with_gif(message: Message):
    """
    This function is triggered when a user sends an animation as a message.

    :param message: The incoming message object
    :type message: aiogram.types.Message
    :return: None
    """
    await message.answer(
        "This message contains an animation, but I don't know how to translate it"
    )
