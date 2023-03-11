from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from tg_bot.loader import dp
from tg_bot.utils import set_commands


@dp.message_handler(CommandStart(), chat_type='private')
async def bot_start(message: types.Message):
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    await set_commands(dp=dp,
                       chat_id=str(message.chat.id))
    await message.answer('\n'.join(
        [
            f"Привет, {message.from_user.full_name}!",
            '',
            'В этом боте представлены функции для получения информации с датчиков и управления системами, установленных в теплице.',
            '',
            'Воспользуйся командами из меню ниже.'
        ]
    ))
