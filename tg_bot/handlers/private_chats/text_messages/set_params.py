from aiogram import types
from aiogram.dispatcher import FSMContext

from db_api import SystemParams
from tg_bot.loader import dp
from tg_bot.states import SetParamsStates


@dp.message_handler(content_types=types.ContentType.TEXT,
                    chat_type=types.ChatType.PRIVATE,
                    role_filter='admin',
                    state=SetParamsStates)
async def get_param_value(message: types.Message, state: FSMContext):
    red_message = (await state.get_data()).get('red_message')
    param_value = (await state.get_data()).get('param_value')
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    try:
        param = float(message.text)
    except:
        try:
            await dp.bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=red_message,
                reply_markup=None,
                text='\n'.join(
                    [
                        'Укажите целое или дробное число. Для дробного числа используйте символ "."',
                        f'\nВведите новое значение для параметра {param_value}'
                    ]
                )
            )
            return
        except:
            return
    if str(await state.get_state()) == 'SetParamsStates:set_request_timeout':
        SystemParams.update(request_timeout=param).where(SystemParams.id == 1).execute()
    elif str(await state.get_state()) == 'SetParamsStates:set_min_air_temp':
        SystemParams.update(min_air_temp=param).where(SystemParams.id == 1).execute()
    elif str(await state.get_state()) == 'SetParamsStates:set_max_air_temp':
        SystemParams.update(max_air_temp=param).where(SystemParams.id == 1).execute()
    elif str(await state.get_state()) == 'SetParamsStates:set_min_air_hum':
        SystemParams.update(min_air_hum=param).where(SystemParams.id == 1).execute()
    elif str(await state.get_state()) == 'SetParamsStates:set_max_air_hum':
        SystemParams.update(max_air_hum=param).where(SystemParams.id == 1).execute()
    elif str(await state.get_state()) == 'SetParamsStates:set_min_ground_hum':
        SystemParams.update(min_ground_hum=param).where(SystemParams.id == 1).execute()
    elif str(await state.get_state()) == 'SetParamsStates:set_max_ground_hum':
        SystemParams.update(max_ground_hum=param).where(SystemParams.id == 1).execute()
    try:
        await dp.bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=red_message,
            reply_markup=None,
            text='\n'.join(
                [
                    f'\nНовое значение для параметра {param_value} установлено равным {param}'
                ]
            )
        )
        await state.finish()
    except:
        await dp.bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=red_message,
            reply_markup=None,
            text='\n'.join(
                [
                    'Что-то пошло не так. Попробуйте еще раз.',
                    f'\nВведите новое значение для параметра {param_value}'
                ]
            )
        )
