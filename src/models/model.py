from functools import lru_cache

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class Translate:
    def __init__(
        self,
        tokenizer_name="Helsinki-NLP/opus-mt-ru-en",
        model_name="Helsinki-NLP/opus-mt-ru-en",
    ) -> None:
        self.load_model(tokenizer_name, model_name)

    def load_model(self, tokenizer_name, model_name):

        try:
            self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
            self.model_max_lenght = self.tokenizer.model_max_length
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        except Exception as e:
            print(f"Error loading model: {e}")

    def tokenize(self, text):
        return self.tokenizer(text=text, return_tensors="pt")

    def generate(self, tokens):
        return self.model.generate(**tokens)

    def decode(self, translation):
        return self.tokenizer.decode(translation[0], skip_special_tokens=True)

    @lru_cache()
    def translate(self, text: str):
        tokens = self.tokenize(text)

        if tokens["input_ids"].shape[1] > self.model_max_lenght:
            return "Мне очень жаль, но ваш текст слишком большой для перевода. Попробуйте сократить его"

        translataion_encoded = self.generate(tokens)
        translataion_decoded = self.decode(translation=translataion_encoded)
        return translataion_decoded


translator = Translate()
