import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from db_api import TempHumValues, TempHumSensor, GroundValues, GroundSensor
from tg_bot.loader import dp
from tg_bot.states import AddValuesStates


@dp.message_handler(content_types=types.ContentType.TEXT,
                    chat_type=types.ChatType.PRIVATE,
                    role_filter='admin',
                    state=AddValuesStates.wait_for_air_temp_values)
async def get_air_temp_values(message: types.Message, state: FSMContext):
    temp_hum_data = dict()
    red_message = (await state.get_data()).get('red_message')
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    try:
        if len(message.text.split(' ')) != 4:
            raise Exception()
        temp_list = list(map(float, message.text.split(' ')))
    except:
        try:
            red_message = await dp.bot.edit_message_text(chat_id=message.chat.id,
                                                         message_id=red_message,
                                                         reply_markup=None,
                                                         text='\n'.join(
                                                             [
                                                                 '<b>Проверьте правильность и формат присланных данных!</b>\n'
                                                                 'Пришлите данные температуры для 4х датчиков одним сообщением в одну строку, разделяя показания символом пробела.',
                                                                 '\n<i>Для дробных чисел используйте символ "."</i>',
                                                                 '\nПример сообщения:',
                                                                 '<b><i>25.4 26.2 25.9 26</i></b>'
                                                             ]
                                                         ))
            return
        except:
            pass
    temp_hum_data['temperature'] = temp_list
    try:
        red_message = await dp.bot.edit_message_text(chat_id=message.chat.id,
                                                     message_id=red_message,
                                                     reply_markup=None,
                                                     text='\n'.join(
                                                         [
                                                             'Показания датчиков температуры приняты!'
                                                             'Пришлите данные влажности для 4х датчиков одним сообщением в одну строку, разделяя показания символом пробела.',
                                                             '\n<i>Для дробных чисел используйте символ "."</i>',
                                                             '\nПример сообщения:',
                                                             '<b><i>50.4 54.2 55.9 56</i></b>'
                                                         ]
                                                     ))
    except:
        pass
    await AddValuesStates.wait_for_air_hum_values.set()
    await state.update_data(red_message=red_message.message_id)
    await state.update_data(temp_hum_data=temp_hum_data)


@dp.message_handler(content_types=types.ContentType.TEXT,
                    chat_type=types.ChatType.PRIVATE,
                    role_filter='admin',
                    state=AddValuesStates.wait_for_air_hum_values)
async def get_air_hum_values(message: types.Message, state: FSMContext):
    red_message = (await state.get_data()).get('red_message')
    temp_hum_data = (await state.get_data()).get('temp_hum_data')
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    try:
        if len(message.text.split(' ')) != 4:
            raise Exception()
        hum_list = list(map(float, message.text.split(' ')))
    except:
        try:
            red_message = await dp.bot.edit_message_text(chat_id=message.chat.id,
                                                         message_id=red_message,
                                                         reply_markup=None,
                                                         text='\n'.join(
                                                             [
                                                                 '<b>Проверьте правильность и формат присланных данных!</b>\n'
                                                                 'Пришлите данные влажности для 4х датчиков одним сообщением в одну строку, разделяя показания символом пробела.',
                                                                 '\n<i>Для дробных чисел используйте символ "."</i>',
                                                                 '\nПример сообщения:',
                                                                 '<b><i>25.4 26.2 25.9 26</i></b>'
                                                             ]
                                                         ))
            return
        except:
            pass
    temp_hum_data['humidity'] = hum_list
    TempHumValues.create(
        timestamp=datetime.datetime.now(),
        sensor1=TempHumSensor.create(
            temperature=temp_hum_data.get('temperature')[0],
            humidity=temp_hum_data.get('humidity')[0]
        ),
        sensor2=TempHumSensor.create(
            temperature=temp_hum_data.get('temperature')[1],
            humidity=temp_hum_data.get('humidity')[1]
        ),
        sensor3=TempHumSensor.create(
            temperature=temp_hum_data.get('temperature')[2],
            humidity=temp_hum_data.get('humidity')[2]
        ),
        sensor4=TempHumSensor.create(
            temperature=temp_hum_data.get('temperature')[3],
            humidity=temp_hum_data.get('humidity')[3]
        ),
    )
    # try:
    await dp.bot.edit_message_text(chat_id=message.chat.id,
                                   message_id=red_message,
                                   reply_markup=None,
                                   text='\n'.join(
                                       [
                                           'Показания датчиков температуры и влажности воздуха приняты!'
                                       ]
                                   ))
    # except:
    #     pass
    await state.finish()


@dp.message_handler(content_types=types.ContentType.TEXT,
                    chat_type=types.ChatType.PRIVATE,
                    role_filter='admin',
                    state=AddValuesStates.wait_for_ground_hum_values)
async def get_air_ground_values(message: types.Message, state: FSMContext):
    red_message = (await state.get_data()).get('red_message')
    ground_hum_data = dict()
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    try:
        if len(message.text.split(' ')) != 6:
            raise Exception()
        hum_list = list(map(float, message.text.split(' ')))
    except:
        try:
            red_message = await dp.bot.edit_message_text(chat_id=message.chat.id,
                                                         message_id=red_message,
                                                         reply_markup=None,
                                                         text='\n'.join(
                                                             [
                                                                 '<b>Проверьте правильность и формат присланных данных!</b>\n'
                                                                 'Пришлите данные влажности почвы для 6и датчиков одним сообщением в одну строку, разделяя показания символом пробела.',
                                                                 '\n<i>Для дробных чисел используйте символ "."</i>',
                                                                 '\nПример сообщения:',
                                                                 '<b><i>25.4 26.2 25.9 26 25.9 26</i></b>'
                                                             ]
                                                         ))
            return
        except:
            pass
    ground_hum_data['humidity'] = hum_list
    GroundValues.create(
        timestamp=datetime.datetime.now(),
        sensor1=GroundSensor.create(
            humidity=ground_hum_data.get('humidity')[0]
        ),
        sensor2=GroundSensor.create(
            humidity=ground_hum_data.get('humidity')[1]
        ),
        sensor3=GroundSensor.create(
            humidity=ground_hum_data.get('humidity')[2]
        ),
        sensor4=GroundSensor.create(
            humidity=ground_hum_data.get('humidity')[3]
        ),
        sensor5=GroundSensor.create(
            humidity=ground_hum_data.get('humidity')[4]
        ),
        sensor6=GroundSensor.create(
            humidity=ground_hum_data.get('humidity')[5]
        ),
    )
    try:
        red_message = await dp.bot.edit_message_text(chat_id=message.chat.id,
                                                     message_id=red_message,
                                                     reply_markup=None,
                                                     text='\n'.join(
                                                         [
                                                             'Показания датчиков влажности почвы приняты!'
                                                         ]
                                                     )
                                                     )
    except:
        pass
    await state.finish()
