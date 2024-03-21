from aiogram import Router

from . import start
from . import different_types
from . import ratings
from . import statistics
from . import translate


def get_routers() -> "list[Router]":
    return [
        start.router,
        translate.router,
        ratings.router,
        statistics.router,
        different_types.router,
    ]