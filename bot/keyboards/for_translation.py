from aiogram import types


def get_tranlsation_kb() -> types.KeyboardButton:
    """
    :return:
    """
    kb = [
        [
            types.KeyboardButton(text="Отправить на перевод"),
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Введите текст для перевода",
    )
    return keyboard
