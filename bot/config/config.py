from dataclasses import dataclass

from dotenv import load_dotenv

# trunk-ignore(ruff/F401)
from .base import ImproperlyConfigured, getenv


@dataclass
class TelegramBotConfig:
    """
    """
    token: str


@dataclass
class Config:
    """
    """
    tg_bot: TelegramBotConfig


def load_config() -> Config:
    """
    :return:
    """
    # Parse a `.env` file and load the variables into environment valriables
    load_dotenv(dotenv_path="/home/aym/projects/hse/HSE-advanced_python-hw2_TgBot/.env", verbose=True)

    return Config(tg_bot=TelegramBotConfig(token=getenv("BOT_TOKEN")))
