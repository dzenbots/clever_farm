import logging

from aiogram import Dispatcher

from data import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот запущен")
        except Exception:
            pass


async def on_shutdown_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот остановлен")
        except Exception:
            pass
