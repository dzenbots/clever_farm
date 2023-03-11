import asyncio
import datetime

from farm_api_module import FarmApiModule
from db_api import TempHumSensor, TempHumValues, GroundSensor, GroundValues, SystemParams


async def get_metric():
    farm_module = FarmApiModule()
    cur_air_temp_hum = list()
    tem_hum_values = dict()
    cur_ground_hum = list()
    ground_hum_values = dict()
    system_params: SystemParams = SystemParams.select().order_by(SystemParams.id.desc()).limit(1)[0]
    while True:
        for i in range(0, 4):
            cur_air_temp_hum.append(farm_module.get_air_temp_hum(sensor_id=i + 1))
            tem_hum_values[f"{int(cur_air_temp_hum[i].get('id'))}"] = TempHumSensor.create(
                temperature=cur_air_temp_hum[i].get('temperature'),
                humidity=cur_air_temp_hum[i].get('humidity'))
        TempHumValues.create(
            timestamp=datetime.datetime.now(),
            sensor1=tem_hum_values.get('1'),
            sensor2=tem_hum_values.get('2'),
            sensor3=tem_hum_values.get('3'),
            sensor4=tem_hum_values.get('4'),
        )
        for i in range(0, 6):
            cur_ground_hum.append(farm_module.get_ground_hum(sensor_id=i + 1))
            ground_hum_values[f"{int(cur_ground_hum[i].get('id'))}"] = GroundSensor.create(
                humidity=cur_ground_hum[i].get('humidity'))
        GroundValues.create(
            timestamp=datetime.datetime.now(),
            sensor1=ground_hum_values.get('1'),
            sensor2=ground_hum_values.get('2'),
            sensor3=ground_hum_values.get('3'),
            sensor4=ground_hum_values.get('4'),
            sensor5=ground_hum_values.get('5'),
            sensor6=ground_hum_values.get('6'),
        )
        cur_air_temp_hum.clear()
        tem_hum_values.clear()
        cur_ground_hum.clear()
        ground_hum_values.clear()
        await asyncio.sleep(system_params.request_timeout)
