from datetime import datetime

import pytest
from aiogram.dispatcher.event.bases import UNHANDLED
from aiogram.enums import ChatType
from aiogram.methods import SendMessage
from aiogram.methods.base import TelegramType
from aiogram.types import Update, Chat, User, Message
from bot.utils.text import bq
from aiogram.fsm.context import FSMContext
from bot.handlers.translate import TranslateState


def make_message(text: str, user_id = 123456) -> Message:
    user = User(id=user_id, first_name="User", is_bot=False)
    chat = Chat(id=user_id, type=ChatType.PRIVATE)
    return Message(message_id=1, from_user=user, chat=chat, date=datetime.now(), text=text)


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
async def test_cmd_get_stats(dp, bot, rating_instance):
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
        ratings=rating_instance,
        date=datetime.now(),
    )
    result = await dp.feed_update(bot, Update(message=message, update_id=1),  ratings=rating_instance)
    assert result is not UNHANDLED
    outgoing_message: TelegramType = bot.get_request()
    assert isinstance(outgoing_message, SendMessage)
    assert (
        outgoing_message.text
        ==  "Статистика:\n- Пока статистики нет, оцените бот первыми!")

@pytest.mark.asyncio
async def test_translate(dp, bot):
    # Получение контекста FSM для текущего юзера
    chat = Chat(id=1234567, type=ChatType.PRIVATE)
    user = User(id=1234567, username="Username", is_bot=False, first_name="User")

    fsm_context: FSMContext = dp.fsm.get_context(bot=bot, user_id=user.id, chat_id=chat.id)
    await fsm_context.set_state(None)   
    
    bot.add_result_for(
        method=SendMessage,
        ok=True,
    )
    message = Message(
        message_id=1,
        chat=chat,
        from_user=user,
        text="/translate",
        date=datetime.now(),
    )
    result = await dp.feed_update(bot, Update(message=message, update_id=1))
    assert result is not UNHANDLED
    outgoing_message: TelegramType = bot.get_request()
    assert isinstance(outgoing_message, SendMessage)
    assert (
        outgoing_message.text
        == "Введите текст для перевода"
    )

    current_state = await fsm_context.get_state()
    assert current_state == TranslateState.text

    # Отправка корректного значения названия блюда
    bot.add_result_for(SendMessage, ok=True)
    await dp.feed_update(bot, Update(message=make_message("Привет, это тестовое сообщение"), update_id=1))
    bot.get_request()

    current_state = await fsm_context.get_state()
    current_state == 1