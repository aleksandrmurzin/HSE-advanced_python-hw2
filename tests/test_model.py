import pytest

from bot.models.classifier import clf_language
from bot.models.seq2seq import translator
from bot.models.utils.reply import ReplyMessage


@pytest.mark.models
class TestModelClass:
    """Tests ml modles"""

    # def test_raises_error_create_class(self):
    #     """test_raises_error_create_class
    #     """
    #     with pytest.raises(Exception):
    #         Translate().load_model()

    def test_can_download_model(self):
        """test_can_download_model cheking if model was downloaded"""
        assert hasattr(translator, "model")

    def test_can_load_model(self):
        """test_can_load_model checking that link or enternet conn is ok"""
        assert True is translator.loading_flag, "Something went wrong"

    def test_translate_from_russian(self):
        """test_translate_from_russian cheks basic example"""
        assert ReplyMessage("Hey!", True) == translator.predict(text="Привет!")

    def test_translate_from_other_language(self):
        """test_translate_from_other_language cheks basic example for other lang"""
        assert ReplyMessage(
            message="Mне очень жаль, но я умею переводить только с русского языка",
            flag=False,
        ) == translator.predict(text="ウィキペ")

    def test_translate_from_other_language2(self):
        """test_translate_from_other_language2  cheks basic example for other lang???"""
        assert ReplyMessage(message="", flag=True) == clf_language.predict(
            text="Привет, меня зовут:"
        )

    @pytest.mark.slow
    def test_translate_long_text(self):
        """test_translate_long_text cheks long text handling"""
        long_text = """Это очень большой текст, буквально лонг-рид.""" * 10**3
        expected = ReplyMessage(
            "Мне очень жаль, но ваш текст слишком большой для перевода. Попробуйте сократить его",
            False,
        )
        assert expected == translator.predict(text=long_text)
