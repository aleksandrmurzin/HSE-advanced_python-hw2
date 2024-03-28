from aiogram import Router

from . import different_types, ratings, start, statistics, translate


def get_routers() -> "list[Router]":
    return [
        start.router,
        translate.router,
        ratings.router,
        statistics.router,
        different_types.router,
    ]
