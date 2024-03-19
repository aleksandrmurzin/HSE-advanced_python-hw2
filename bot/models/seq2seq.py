from functools import lru_cache

from transformers import AutoModelForSeq2SeqLM

from bot.models.base import HugggingFaceBaseModel
from bot.models.classifier import clf_language
from bot.models.utils.reply import ReplyMessage


class Translate(HugggingFaceBaseModel):
    """
    :param HugggingFaceBaseModel: HugggingFaceBaseModel
    """
    def __init__(
        self,
        tokenizer_name="Helsinki-NLP/opus-mt-ru-en",
        model_name="Helsinki-NLP/opus-mt-ru-en",
        model_task=AutoModelForSeq2SeqLM,
    ) -> None:
        """
        :param tokenizer_name: defaults to "Helsinki-NLP/opus-mt-ru-en"
        :param model_name: defaults to "Helsinki-NLP/opus-mt-ru-en"
        :param model_task: defaults to AutoModelForSeq2SeqLM
        """
        super().__init__(tokenizer_name, model_name, model_task)

    # trunk-ignore(ruff/B019)
    @lru_cache(maxsize=16)
    def predict(self, text: str):
        """
        :param text: text
        :return:
        """
        if not self.loading_flag:
            return ReplyMessage(
                message="Mне очень жаль, но сейчас не получается сделать ваш перевод",
                flag=False,
            )

        tokens = self.tokenize(text)
        if tokens["input_ids"].shape[1] > self.model_max_lenght:
            return ReplyMessage(
                message="Мне очень жаль, но ваш текст слишком большой для перевода. Попробуйте сократить его",
                flag=False,
            )

        result = clf_language.predict(text)
        if not result.flag:
            return result

        translataion_encoded = self.generate(tokens)
        translataion_decoded = self.decode(translation=translataion_encoded)

        return ReplyMessage(message=translataion_decoded, flag=True)


translator = Translate()
