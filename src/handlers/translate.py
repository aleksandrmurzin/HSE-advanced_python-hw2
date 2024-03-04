from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.formatting import Bold, as_list, as_marked_section

from src.models.model import translator

router = Router()


class Translate(StatesGroup):
    text = State()


class Content:
    init = as_list(
        as_marked_section(
            Bold("Статус:"),
            "Перевожу...",
            marker="⏳ ",
        ),
    )

    update = as_list(
        as_marked_section(
            Bold("Статус:"),
            "Успех!",
            marker="✅ ",
        ),
        as_marked_section(
            Bold("Ваш перевод сообщением ниже!"),
            "",
            marker="⬇",
        ),
    )


@router.message(Command(commands=["translate"]))
async def cmd_translate(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Translate.text)
    await message.answer(
        "Введите текст для перевода", reply_markup=types.ReplyKeyboardRemove()
    )


@router.message(Translate.text)
async def process_text(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    init_message = await message.reply(**Content.init.as_kwargs())
    translation = translator.translate(message.text)

    if translation:
        await init_message.edit_text(**Content.update.as_kwargs())
        await message.answer(f"{translation}")

    else:
        ...  # add reject
