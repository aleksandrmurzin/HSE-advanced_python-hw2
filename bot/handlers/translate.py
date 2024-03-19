# trunk-ignore-all(black)
from dataclasses import dataclass

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.formatting import Bold, as_list, as_marked_section

from bot.models.seq2seq import translator

router = Router()


class Translate(StatesGroup):
    """
    :param StatesGroup: StatesGroup
    """
    text = State()


@dataclass
class Content:
    status: bool = True

    @property
    def working_status(self):
        """
        :return:
        """
        return as_list(
            as_marked_section(
                Bold("Статус:"),
                "Перевожу...",
                marker="⏳ ",
            ),
        )

    def status_section(self):
        """
        :return:
        """
        if not self.status:
            return as_marked_section(
                Bold("Статус:"),
                "Перевод не выполнен!",
                marker="⚠️ ",
            )
        return as_marked_section(
            Bold("Статус:"),
            "Успех!",
            marker="✅ ",
        )

    @property
    def updated_status(self):
        """
        :return:
        """
        return as_list(
            self.status_section(),
            as_marked_section(
                "Ответ",
                "",
                marker="⬇",
            ),
        )


@router.message(Command(commands=["translate"]))
async def cmd_translate(message: types.Message, state: FSMContext) -> None:
    """
    :param message: message
    :param state: state
    """
    await state.set_state(Translate.text)
    await message.answer(
        "Введите текст для перевода", reply_markup=types.ReplyKeyboardRemove()
    )


@router.message(F.text, Translate.text)
async def process_text(message: types.Message, state: FSMContext) -> None:
    """
    :param message: message
    :param state: state
    """
    await state.clear()

    init_message = await message.reply(**Content().working_status.as_kwargs())
    result = translator.predict(message.text)

    await init_message.edit_text(
        **Content(status=result.flag).updated_status.as_kwargs()
    )
    await message.answer(f"{result.message}")
