from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.formatting import Bold, as_list, as_marked_section

from bot.utils.evaluate import ratings

router = Router()


def content(text):
    """
    :param text: text
    :return:
    """
    return as_list(
        as_marked_section(
            Bold("Статистика:"),
            text,
        )
    )


@router.message(Command("stats"))
async def cmd_get_info(message: types.Message):
    """
    :param message: message
    """
    statistics = ratings.statistics
    if not isinstance(statistics, dict):
        text = "Пока статистики нет, оцените бот первыми!"
        await message.answer(**content(text).as_kwargs())
    text = f"Средняя оценка перевода {statistics['average_rating']}"
    await message.answer(**content(text).as_kwargs())
