from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from tg_bot.filters import CommandSetParams
from tg_bot.keyboards.inline import set_params_keyboard, set_params_callback
from tg_bot.loader import dp
from tg_bot.states import SetParamsStates


@dp.message_handler(CommandSetParams(), chat_type='private', role_filter='admin')
async def set_params_handler_admin(message: types.Message):
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    await message.answer(text='Выберите параметр для изменения',
                         reply_markup=set_params_keyboard)


@dp.callback_query_handler(set_params_callback.filter(param='request_timeout'),
                           chat_type='private',
                           role_filter='admin')
async def set_param_request_timeout(call: CallbackQuery, state: FSMContext):
    red_message: types.Message = await dp.bot.edit_message_text(chat_id=call.message.chat.id,
                                   message_id=call.message.message_id,
                                   reply_markup=None,
                                   text='Введите время в секундах для задания нового интервала запросов данных с датчиков в теплице')
    await SetParamsStates.set_request_timeout.set()
    await state.update_data(red_message=red_message.message_id)
    await state.update_data(param_value='request_timeout')


@dp.callback_query_handler(set_params_callback.filter(),
                           chat_type='private',
                           role_filter='admin')
async def set_param_current_param(call: CallbackQuery, callback_data: dict, state: FSMContext):
    param = callback_data.get('param')
    arg = callback_data.get('arg')
    if param == 'air_temp':
        if arg == 'min':
            param_value = '<b>Минимальная температура воздуха</b>'
            await SetParamsStates.set_min_air_temp.set()
        if arg == 'max':
            param_value = '<b>Максимальная температура воздуха</b>'
            await SetParamsStates.set_max_air_temp.set()
    elif param == 'air_hum':
        if arg == 'min':
            param_value = '<b>Минимальная влажность воздуха</b>'
            await SetParamsStates.set_min_air_hum.set()
        if arg == 'max':
            param_value = '<b>Максимальная влажность воздуха</b>'
            await SetParamsStates.set_max_air_hum.set()
    elif param == 'ground_hum':
        if arg == 'min':
            param_value = '<b>Минимальная влажность почвы</b>'
            await SetParamsStates.set_min_ground_hum.set()
        if arg == 'max':
            param_value = '<b>Максимальная влажность почвы</b>'
            await SetParamsStates.set_max_ground_hum.set()
    red_message: types.Message = await dp.bot.edit_message_text(chat_id=call.message.chat.id,
                                                                message_id=call.message.message_id,
                                                                reply_markup=None,
                                                                text=f'Введите новое значение для параметра {param_value}')
    await state.update_data(red_message=red_message.message_id)
    await state.update_data(param_value=param_value)


@dp.callback_query_handler(set_params_callback.filter(param='no_action'))
async def set_param_no_action(call: CallbackQuery):
    await call.answer(cache_time=1)


@dp.message_handler(CommandSetParams(), chat_type='private')
async def set_params_handler_no_admin(message: types.Message):
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    await message.answer(text='Команда доступна только администраторам',
                         reply_markup=None)
