# trunk-ignore-all(black)
from dataclasses import dataclass

from functools import lru_cache
from collections import defaultdict
from src.models.base import HugggingFaceBaseModel
from transformers import AutoModelForSequenceClassification, TextClassificationPipeline
from src.models.utils.reply import ReplyMessage


@dataclass
class MessageLanguge:
    codes2langs = {
        "af-ZA": "Afrikaans",
        "am-ET": "Amharic",
        "ar-SA": "Arabic",
        "az-AZ": "Azeri",
        "bn-BD": "Bengali",
        "zh-CN": "Chinese",
        "zh-TW": "Chinese - Taiwan",
        "da-DK": "Danish",
        "de-DE": "German",
        "el-GR": "Greek",
        "en-US": "English",
        "es-ES": "Spanish",
        "fa-IR": "Farsi",
        "fi-FI": "Finnish",
        "fr-FR": "French",
        "he-IL": "Hebrew",
        "hu-HU": "Hungarian",
        "hy-AM": "Armenian",
        "id-ID": "Indonesian",
        "is-IS": "Icelandic",
        "it-IT": "Italian",
        "ja-JP": "Japanese",
        "jv-ID": "Javanese",
        "ka-GE": "Georgian",
        "km-KH": "Khmer",
        "ko-KR": "Korean",
        "lv-LV": "Latvian",
        "mn-MN": "Mongolian",
        "ms-MY": "Malay",
        "my-MM": "Burmese",
        "nb-NO": "Norwegian",
        "nl-NL": "Dutch",
        "pl-PL": "Polish",
        "pt-PT": "Portuguese",
        "ro-RO": "Romanian",
        "ru-RU": "Russian",
        "sl-SI": "Slovenian",
        "sq-AL": "Albanian",
        "sv-SE": "Swedish",
        "sw-KE": "Swahili",
        "hi-IN": "Hindi",
        "kn-IN": "Kannada",
        "ml-IN": "Malayalam",
        "ta-IN": "Tamil",
        "te-IN": "Telugu",
        "th-TH": "Thai",
        "tl-PH": "Tagalog",
        "tr-TR": "Turkish",
        "ur-PK": "Urdu",
        "vi-VN": "Vietnamese",
        "cy-GB": "Welsh",
    }


class LanguageClassifier(HugggingFaceBaseModel):
    def __init__(
        self,
        tokenizer_name="qanastek/51-languages-classifier",
        model_name="qanastek/51-languages-classifier",
        model_type=AutoModelForSequenceClassification,
    ) -> None:
        super().__init__(tokenizer_name, model_name, model_type)

    @property
    def clf_pipeline(self):
        return TextClassificationPipeline(model=self.model, tokenizer=self.tokenizer)

    # trunk-ignore(ruff/B019)
    @lru_cache()
    def predict(self, text):
        if not self.loading_flag:
            return ReplyMessage(
                message="Mне очень жаль, но сейчас не получается сделать ваш перевод",
                flag=False,
            )

        result = self.clf_pipeline(text)[0]

        if (
            not MessageLanguge.codes2langs[result["label"]] == "Russian"
            or result["score"] < 0.90
        ):
            return ReplyMessage(
                message="Mне очень жаль, но я умею переводить только с русского языка",
                flag=False,
            )
        return ReplyMessage(
            message="",
            flag=True,
        )


clf_language = LanguageClassifier()
