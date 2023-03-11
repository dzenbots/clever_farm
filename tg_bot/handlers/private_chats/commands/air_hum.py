from aiogram import types
from aiogram.types import CallbackQuery

from graph_creator import GraphCreator
from tg_bot.filters.commands import CommandAirHum
from tg_bot.keyboards.inline import choose_sensor_callback_data, get_air_temp_hum_keyboard
from tg_bot.loader import dp
from tg_bot.utils.Misc import get_reverse_list
from db_api import TempHumValues

hum_sensor_list = set()


@dp.message_handler(CommandAirHum(), chat_type='private')
async def air_hum_request(message: types.Message):
    await dp.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)
    global hum_sensor_list
    hum_sensor_list.clear()
    await message.answer(text='Выберите, информацию с каких датчиков влажности Вы хотите получить',
                         reply_markup=get_air_temp_hum_keyboard(param='hum', sensor_list=hum_sensor_list))


@dp.callback_query_handler(choose_sensor_callback_data.filter(param='hum'))
async def add_item_to_air_hum_list(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=1)
    action = callback_data.get('action').split('_')[0]
    sensor_id = int(callback_data.get('action').split('_')[1])
    global hum_sensor_list
    hum_sensor_list.add(sensor_id) if action == 'add' else hum_sensor_list.remove(sensor_id)
    await dp.bot.edit_message_reply_markup(
        reply_markup=get_air_temp_hum_keyboard(param='hum', sensor_list=hum_sensor_list),
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )


@dp.callback_query_handler(choose_sensor_callback_data.filter(param='complete_hum'))
async def send_air_hum_info(call: CallbackQuery):
    global hum_sensor_list
    sensor_values = TempHumValues.select().order_by(TempHumValues.id.desc()).limit(10)
    message_text = list()
    for sensor_num in hum_sensor_list:
        if sensor_num == 5:
            message_text.append('\n\nСредние значения влажности воздуха')
            message_text.append(
                '\n'.join(
                    [
                        f"<b>{sensor_value.timestamp.split('.')[0]}</b> : " +
                        f"{round((sensor_value.sensor1.humidity + sensor_value.sensor2.humidity + sensor_value.sensor3.humidity + sensor_value.sensor4.humidity) / 4, 2)}"
                        for sensor_value in sensor_values
                    ]

                ))
        else:
            message_text.append(f'\n\nПоказания с {sensor_num} датчика влажности')
            message_text.append(
                '\n'.join(
                    [
                        f"<b>{sensor_value.timestamp.split('.')[0]}</b> : " +
                        f"{sensor_value.sensor1.humidity if sensor_num == 1 else sensor_value.sensor2.humidity if sensor_num == 2 else sensor_value.sensor3.humidity if sensor_num == 3 else sensor_value.sensor4.humidity}"
                        for sensor_value in sensor_values
                    ]
                )
            )
    await dp.bot.edit_message_text(chat_id=call.message.chat.id,
                                   message_id=call.message.message_id,
                                   reply_markup=None,
                                   text='\n'.join(message_text))
    data_x = get_reverse_list([sensor_value.timestamp.split(' ')[1].split('.')[0] for sensor_value in sensor_values])
    data = list()
    for sensor_num in hum_sensor_list:
        data.append(
            {
                'label': "Средние значения",
                'data_x': data_x,
                'data_y': get_reverse_list([
                    round((sensor_value.sensor1.humidity + sensor_value.sensor2.humidity + sensor_value.sensor3.humidity + sensor_value.sensor4.humidity) / 4,
                          2)
                    for sensor_value in sensor_values
                ])
            } if sensor_num == 5 else {
                'label': f"Датчик влажности {sensor_num}",
                'data_x': data_x,
                'data_y': get_reverse_list([
                    sensor_value.sensor1.humidity if sensor_num == 1 else sensor_value.sensor2.humidity if sensor_num == 2 else sensor_value.sensor3.humidity if sensor_num == 3 else sensor_value.sensor4.humidity
                    for sensor_value in sensor_values
                ])
            }
        )
    graph_creator = GraphCreator()
    graph_creator.create_graph(data=data, output_filename='air_hum.png')
    await dp.bot.send_photo(photo=open('air_hum.png', "rb"),
                            chat_id=call.message.chat.id)
