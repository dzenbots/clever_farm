from requests import Session


class FarmApiModule(Session):
    def __init__(self):
        super().__init__()

    def get_air_temp_hum(self, sensor_id):
        if sensor_id < 1 or sensor_id > 4:
            return None
        try:
            response = self.get(url=f'https://dt.miet.ru/ppo_it/api/temp_hum/{sensor_id}')
            if response.status_code == 200:
                return response.json()
        except:
            pass
        return None

    def get_ground_hum(self, sensor_id):
        if sensor_id < 1 or sensor_id > 6:
            return None
        try:
            response = self.get(url=f'https://dt.miet.ru/ppo_it/api/hum/{sensor_id}')
            if response.status_code == 200:
                return response.json()
        except:
            pass
        return None

    def control_windows(self, state):
        if state < 0 or state > 1:
            return None
        try:
            response = self.patch(url='https://dt.miet.ru/ppo_it/api/fork_drive',
                                  params={
                                      'state': str(state)
                                  })
            if response.status_code == 200:
                return response.json()
        except:
            pass
        return None

    def control_watering(self, pomp_id, state):
        if pomp_id < 1 or pomp_id > 6:
            return None
        if state < 0 or state > 1:
            return None
        try:
            response = self.patch(url='https://dt.miet.ru/ppo_it/api/watering',
                                  params={
                                      'id': str(pomp_id),
                                      'state': str(state)
                                  })
            if response.status_code == 200:
                return response.json()
        except:
            pass
        return None

    def control_humidity_system(self, state):
        if state < 0 or state > 1:
            return None
        try:
            response = self.patch(url='https://dt.miet.ru/ppo_it/api/total_hum',
                                  params={
                                      'state': str(state)
                                  })
            if response.status_code == 200:
                return response.json()
        except:
            pass
        return None


if __name__ == '__main__':
    apiModule = FarmApiModule()
    print(apiModule.get_air_temp_hum(2))
    print(apiModule.get_ground_hum(3))
    print(apiModule.control_windows(1))
    print(apiModule.control_watering(1, 1))
    print(apiModule.control_humidity_system(1))

