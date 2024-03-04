from datetime import datetime

from aiogram import F, Router, types
from aiogram.filters import Command

from src.keyboards.for_raiting import get_github_url_kb, get_rating_kb
from src.utils.evaluate import ratings

router = Router()  # [1]


@router.message(Command("rate_project"))
async def cmd_rate_project(message: types.Message):
    await message.answer(
        "Если вам понравился проект, поставьте ему ⭐ на GitHub",
        reply_markup=get_github_url_kb(),
    )


@router.message(Command("rate_translation"))
async def cmd_rate_translation(message: types.Message):
    await message.answer(
        "Оцените перевод: 1 - очень плохо, 5 - отлично",
        reply_markup=get_rating_kb(),
    )


@router.callback_query(F.data.contains("_rating"))
async def receive_rating(callback: types.CallbackQuery):
    ratings.update(
        callback.from_user.id, callback.data.split("_rating")[0], datetime.now()
    )

    await callback.answer("Спасибо за оценку!", cache_time=6)
    await callback.message.delete()
