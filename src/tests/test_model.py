import pytest
from src.models.utils.reply import ReplyMessage
from src.models.seq2seq import translator
from src.models.classifier import clf_language
from src.models.seq2seq import Translate


@pytest.mark.models
class TestModelClass:
    def test_raises_error_create_class(self):
        with pytest.raises(Exception):
            Translate().load_model()

    def test_can_download_model(self):
        assert hasattr(translator, "model")


    def test_can_load_model(self):
        assert True == translator.loading_flag, "Something went wrong"


    def test_translate_from_russian(self):
        assert ReplyMessage("Hey!", True) == translator.predict(text="Привет!")


    def test_translate_from_other_language(self):  # TODO FIX
        # trunk-ignore(bandit/B101)
        assert ReplyMessage(
                    message="Mне очень жаль, но я умею переводить только с русского языка",
                    flag=False,
                ) == translator.predict(text="ウィキペ")


    def test_translate_from_other_language2(self):  # TODO FIX
        # trunk-ignore(bandit/B101)
        assert ReplyMessage(message="", flag=True) == clf_language.predict(
            text="Привет, меня зовут:"
        )


    @pytest.mark.slow
    def test_translate_long_text(self):
        long_text = """Это очень большой текст, буквально лонг-рид.""" * 10**3
        expected = ReplyMessage(
            "Мне очень жаль, но ваш текст слишком большой для перевода. Попробуйте сократить его",
            False,
        )
        # trunk-ignore(bandit/B101)
        assert expected == translator.predict(text=long_text)
