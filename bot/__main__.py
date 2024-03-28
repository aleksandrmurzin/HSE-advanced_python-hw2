#!/usr/bin/env python3

import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.config import Config, load_config
from bot.handlers import different_types, ratings, start, statistics, translate

logging.basicConfig(level=logging.INFO)


# Запуск бота
async def main():
    """ """
    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dispatcher = Dispatcher()
    dispatcher.include_routers(
        start.router,
        translate.router,
        ratings.router,
        statistics.router,
        different_types.router,
    )

    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
