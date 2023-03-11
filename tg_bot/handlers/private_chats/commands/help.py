from aiogram import types
from aiogram.dispatcher.filters import CommandHelp

from tg_bot.loader import dp


@dp.message_handler(CommandHelp(), chat_type='private')
async def air_temp_request(message: types.Message):
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    await message.answer(text='Здесь будет справка по работе бота. To be continued...')
