from datetime import datetime

import pytest
from aiogram.dispatcher.event.bases import UNHANDLED
from aiogram.enums import ChatType
from aiogram.fsm.context import FSMContext
from aiogram.methods import SendMessage, AnswerCallbackQuery
from aiogram.methods.base import TelegramType
from aiogram.types import Chat, Message, Update, User, CallbackQuery

from bot.handlers.translate import TranslateState
from bot.utils.text import bq

USER_ID = 12345
USER = User(id=USER_ID, first_name="User", is_bot=False, username="user")
CHAT = Chat(id=USER_ID, type=ChatType.PRIVATE)


def make_message(text: str, user=USER, chat=CHAT) -> Message:
    """_summary_

    :param str text: _description_
    :param _type_ user: _description_, defaults to USER
    :param _type_ chat: _description_, defaults to CHAT
    :return Message: _description_
    """
    return Message(
        message_id=1, from_user=user, chat=chat, date=datetime.now(), text=text
    )


@pytest.mark.asyncio
async def test_cmd_start(dp, bot):
    bot.add_result_for(
        method=SendMessage,
        ok=True,
    )
    message = make_message(text="/start")

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
    """"""
    bot.add_result_for(
        method=SendMessage,
        ok=True,
    )
    message = make_message(text="/rate_translation")

    result = await dp.feed_update(bot, Update(message=message, update_id=1))
    assert result is not UNHANDLED
    outgoing_message: TelegramType = bot.get_request()
    assert isinstance(outgoing_message, SendMessage)
    assert outgoing_message.text == "Оцените перевод: 1 - очень плохо, 5 - отлично"


@pytest.mark.asyncio
async def test_rate_project(dp, bot):
    """"""
    bot.add_result_for(
        method=SendMessage,
        ok=True,
    )

    message = make_message(text="/rate_project")
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
    """"""
    bot.add_result_for(
        method=SendMessage,
        ok=True,
    )
    message = make_message(text="/stats")
    result = await dp.feed_update(
        bot, Update(message=message, update_id=1), ratings=rating_instance
    )
    assert result is not UNHANDLED
    outgoing_message: TelegramType = bot.get_request()
    assert isinstance(outgoing_message, SendMessage)
    assert (
        outgoing_message.text
        == "Статистика:\n- Пока статистики нет, оцените бот первыми!"
    )


@pytest.mark.asyncio
async def test_cmd_get_stats_2(dp, bot, rating_instance):
    """"""
    rating_instance.update(9999, 4, "2024-03-21")

    bot.add_result_for(
        method=SendMessage,
        ok=True,
    )
    message = make_message(text="/stats")
    result = await dp.feed_update(
        bot, Update(message=message, update_id=1), ratings=rating_instance
    )
    assert result is not UNHANDLED
    outgoing_message: TelegramType = bot.get_request()
    assert isinstance(outgoing_message, SendMessage)
    assert outgoing_message.text == "Статистика:\n- Средняя оценка перевода 4.0"


@pytest.mark.asyncio
async def test_translate_1(dp, bot, user=USER, chat=USER):
    """"""
    fsm_context: FSMContext = dp.fsm.get_context(
        bot=bot, user_id=user.id, chat_id=chat.id
    )
    await fsm_context.set_state(None)

    bot.add_result_for(method=SendMessage, ok=True)
    result = await dp.feed_update(
        bot, Update(message=make_message("/translate"), update_id=1)
    )

    current_state = await fsm_context.get_state()
    assert current_state == TranslateState.text

    assert result is not UNHANDLED

    outgoing_message: TelegramType = bot.get_request()
    assert isinstance(outgoing_message, SendMessage)
    assert outgoing_message.text == "Введите текст для перевода"
