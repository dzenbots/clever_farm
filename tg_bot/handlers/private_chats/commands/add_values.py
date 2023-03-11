from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from tg_bot.filters import CommandAddValues
from tg_bot.keyboards.inline import add_values_keyboard, add_values_callback_data
from tg_bot.loader import dp
from tg_bot.states import AddValuesStates


@dp.message_handler(CommandAddValues(), chat_type='private', role_filter='admin')
async def add_values_admin(message: types.Message):
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    await message.answer(text='Выберите, данные каких датчиков вы хотите внести вручную',
                         reply_markup=add_values_keyboard)


@dp.callback_query_handler(
    add_values_callback_data.filter(param='temp_hum'),
    chat_type='private',
    role_filter='admin'
)
async def add_temp_hum_values(call: CallbackQuery, state: FSMContext):
    red_message = await dp.bot.edit_message_text(chat_id=call.message.chat.id,
                                                 message_id=call.message.message_id,
                                                 reply_markup=None,
                                                 text='\n'.join(
                                                     [
                                                         'Пришлите данные температуры для 4х датчиков одним сообщением в одну строку, разделяя показания символом пробела.',
                                                         '\n<i>Для дробных чисел используйте символ "."</i>',
                                                         '\nПример сообщения:',
                                                         '<b><i>25.4 26.2 25.9 26</i></b>'
                                                     ]
                                                 ))
    await AddValuesStates.wait_for_air_temp_values.set()
    await state.update_data(red_message=red_message.message_id)


@dp.callback_query_handler(
    add_values_callback_data.filter(param='ground_hum'),
    chat_type='private',
    role_filter='admin'
)
async def add_ground_hum_values(call: CallbackQuery, state: FSMContext):
    red_message = await dp.bot.edit_message_text(chat_id=call.message.chat.id,
                                                 message_id=call.message.message_id,
                                                 reply_markup=None,
                                                 text='\n'.join(
                                                     [
                                                         'Пришлите данные влажности почвы для 6и датчиков одним сообщением в одну строку, разделяя показания символом пробела.',
                                                         '\n<i>Для дробных чисел используйте символ "."</i>',
                                                         '\nПример сообщения:',
                                                         '<b><i>50.4 54.2 55.9 56 55.9 56</i></b>'
                                                     ]
                                                 ))
    await AddValuesStates.wait_for_ground_hum_values.set()
    await state.update_data(red_message=red_message.message_id)


@dp.message_handler(CommandAddValues(), chat_type='private')
async def add_values_no_admin(message: types.Message):
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    await message.answer(text='Команда /add_values доступна только администраторам')
