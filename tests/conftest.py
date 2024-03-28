import pytest
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot.handlers import get_routers
from bot.utils.data import Rating
from tests.mocked_aiogram import MockedBot, MockedSession


@pytest.fixture(scope="session")
def dp() -> Dispatcher:
    dispatcher = Dispatcher(storage=MemoryStorage())
    dispatcher.include_routers(*get_routers())
    return dispatcher


@pytest.fixture(scope="session")
def bot() -> MockedBot:
    bot = MockedBot()
    bot.session = MockedSession()
    return bot


@pytest.fixture(scope="session")
def rating_instance(tmp_path_factory):
    """
    :param tmp_path_factory: tmp_path_factory
    :return:
    """
    fn = tmp_path_factory.mktemp("data")
    rating = Rating(path=fn, file="scores.csv")
    return rating
