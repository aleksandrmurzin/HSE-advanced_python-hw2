from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.formatting import Bold, as_list, as_marked_section

from bot.utils.data import Rating

router = Router()
ratings = Rating()


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
async def cmd_get_stats(message: types.Message, ratings):
    """
    :param message: message
    """
    statistics = ratings.statistics
    if not isinstance(statistics, dict):
        text = "Пока статистики нет, оцените бот первыми!"
        await message.answer(**content(text).as_kwargs())
    else:
        text = f"Средняя оценка перевода {statistics['average_rating']}"
        await message.answer(**content(text).as_kwargs())
