from datetime import datetime

import pytest
from aiogram.dispatcher.event.bases import UNHANDLED
from aiogram.enums import ChatType
from aiogram.methods import SendMessage
from aiogram.methods.base import TelegramType
from aiogram.types import Update, Chat, User, Message
from bot.utils.text import bq





@pytest.mark.asyncio
async def test_cmd_start(dp, bot):

    chat = Chat(id=1234567, type=ChatType.PRIVATE)
    user = User(id=1234567, username="Username", is_bot=False, first_name="User")

    bot.add_result_for(
        method=SendMessage,
        ok=True,
    )

    message = Message(
        message_id=1,
        chat=chat,
        from_user=user,
        text="/start",
        date=datetime.now(),
    )
    result = await dp.feed_update(bot, Update(message=message, update_id=1))
    assert result is not UNHANDLED
    outgoing_message: TelegramType = bot.get_request()
    assert isinstance(outgoing_message, SendMessage)
    assert (
        outgoing_message.text
        == f"""Здравствуйте {bq(message.from_user.username)}!
\nЭтот бот поможет Вам перевести текст с Русского на Английский!
\nДля того чтобы начать нажмите /translate и следуйте инструкции.
"""
    )


@pytest.mark.asyncio
async def test_rate_translation(dp, bot):
    chat = Chat(id=1234567, type=ChatType.PRIVATE)
    user = User(id=1234567, username="Username", is_bot=False, first_name="User")

    bot.add_result_for(
        method=SendMessage,
        ok=True,
    )
    message = Message(
        message_id=1,
        chat=chat,
        from_user=user,
        text="/rate_translation",
        date=datetime.now(),
    )
    result = await dp.feed_update(bot, Update(message=message, update_id=1))
    assert result is not UNHANDLED
    outgoing_message: TelegramType = bot.get_request()
    assert isinstance(outgoing_message, SendMessage)
    assert outgoing_message.text == "Оцените перевод: 1 - очень плохо, 5 - отлично"


@pytest.mark.asyncio
async def test_rate_project(dp, bot):
    chat = Chat(id=1234567, type=ChatType.PRIVATE)
    user = User(id=1234567, username="Username", is_bot=False, first_name="User")
    
    bot.add_result_for(
        method=SendMessage,
        ok=True,
    )
    message = Message(
        message_id=1,
        chat=chat,
        from_user=user,
        text="/rate_project",
        date=datetime.now(),
    )
    result = await dp.feed_update(bot, Update(message=message, update_id=1))
    assert result is not UNHANDLED
    outgoing_message: TelegramType = bot.get_request()
    assert isinstance(outgoing_message, SendMessage)
    assert (
        outgoing_message.text
        == "Если вам понравился проект, поставьте ему ⭐ на GitHub"
    )


@pytest.mark.asyncio
async def test_statistics(dp, bot):
    chat = Chat(id=1234567, type=ChatType.PRIVATE)
    user = User(id=1234567, username="Username", is_bot=False, first_name="User")
    
    bot.add_result_for(
        method=SendMessage,
        ok=True,
    )
    message = Message(
        message_id=1,
        chat=chat,
        from_user=user,
        text="/stats",
        date=datetime.now(),
    )
    result = await dp.feed_update(bot, Update(message=message, update_id=1))
    assert result is not UNHANDLED
