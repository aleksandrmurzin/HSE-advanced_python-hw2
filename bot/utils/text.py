"""Configuration for the Telegram bot."""
from aiogram import html


def bq(message):
    """
    :param message: message
    :return:
    """
    return html.bold(html.quote(message))
