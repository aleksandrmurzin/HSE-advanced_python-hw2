from abc import ABC, abstractmethod

from transformers import AutoTokenizer


class HugggingFaceBaseModel(ABC):
    def __init__(
        self,
        tokenizer_name: str,
        model_name: str,
        model_type,
    ) -> None:

        self.load_model(tokenizer_name, model_name, model_type)

    def load_model(self, tokenizer_name, model_name, model_type):

        try:
            self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
            self.model_max_lenght = self.tokenizer.model_max_length
            self.model = model_type.from_pretrained(model_name)
            self.loading_flag = True
        except Exception as e:
            self.loading_flag = False
            print(f"Error loading model: {e}")

    def tokenize(self, text):
        return self.tokenizer(text=text, return_tensors="pt")

    def generate(self, tokens):
        return self.model.generate(**tokens)

    def decode(self, translation):
        return self.tokenizer.decode(translation[0], skip_special_tokens=True)

    @abstractmethod
    def predict(self):
        ...