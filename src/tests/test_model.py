from ..models.model import translator


def test_translate():
    assert "Hey!" == translator.translate(text="Привет!")
