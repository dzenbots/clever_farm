from aiogram import types, Dispatcher
from aiogram.types import BotCommandScopeChat

from data import ADMINS


async def set_commands(dp: Dispatcher, chat_id: str):
    await dp.bot.set_my_commands(
        commands=
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("airtemp", "Температура воздуха"),
            types.BotCommand("airhum", "Влажность воздуха"),
            types.BotCommand("groundhum", "Влажность грунта"),
            types.BotCommand("help", "Вывести справку"),
        ] if chat_id not in ADMINS else
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("airtemp", "Температура воздуха"),
            types.BotCommand("airhum", "Влажность воздуха"),
            types.BotCommand("groundhum", "Влажность грунта"),
            types.BotCommand("control", "Управление"),
            types.BotCommand("force_control", "Принудительное управление"),
            types.BotCommand('add_values', "Добавить показания датчиков"),
            types.BotCommand('set_params', "Изменить параметры"),
            types.BotCommand("help", "Вывести справку"),
        ],
        scope=BotCommandScopeChat(
            chat_id=chat_id
        )
    )
