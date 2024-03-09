from aiogram import html


def bq(message):
    return html.bold(html.quote(message))
