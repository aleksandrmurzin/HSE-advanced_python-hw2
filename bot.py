#!/usr/bin/env python3

import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import Config, load_config
from src.handlers import different_types, example, ratings, start, statistics, translate

logging.basicConfig(level=logging.INFO)


# Запуск бота
async def main():
    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(
        start.router,
        translate.router,
        ratings.router,
        different_types.router,
        example.router,
        statistics.router,
    )

    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
