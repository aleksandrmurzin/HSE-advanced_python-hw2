import pytest

from ..models.seq2seq import translator


def test_translate_from_russian():
    assert ("Hey!", True) == translator.translate(text="Привет!")


def test_translate_from_other_language():  # TODO FIX
    # trunk-ignore(bandit/B101)
    assert translator.translate(text="ウィキペ") == translator.translate(
        text="ウィキペ"
    )


@pytest.mark.slow
def test_translate_long_text():
    long_text = """Это очень большой текст, буквально лонг-рид.""" * 10**3
    expected = (
        "Мне очень жаль, но ваш текст слишком большой для перевода. Попробуйте сократить его",
        False,
    )
    # trunk-ignore(bandit/B101)
    assert expected == translator.translate(text=long_text)
