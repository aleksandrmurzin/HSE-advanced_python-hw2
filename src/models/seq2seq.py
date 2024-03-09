from functools import lru_cache
from src.models.base import HugggingFaceBaseModel
from transformers import AutoModelForSeq2SeqLM
from src.models.classifier import clf_language
from src.models.utils.reply import ReplyMessage

class Translate(HugggingFaceBaseModel):
    def __init__(
        self,
        tokenizer_name="Helsinki-NLP/opus-mt-ru-en",
        model_name="Helsinki-NLP/opus-mt-ru-en",
        model_task=AutoModelForSeq2SeqLM,
    ) -> None:
        super().__init__(tokenizer_name, model_name, model_task)

    @lru_cache()
    def predict(self, text: str):
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
        
        return ReplyMessage(
            message=translataion_decoded,
            flag=True)


translator = Translate()
