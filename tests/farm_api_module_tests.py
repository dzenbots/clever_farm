import unittest

import requests

from farm_api_module import FarmApiModule


class BasicModuleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.api_module = FarmApiModule()

    def tearDown(self) -> None:
        self.api_module.close()

    def test_temperature(self):
        self.assertEqual(None, self.api_module.get_air_temp_hum(sensor_id=5))
        self.assertEqual(None, self.api_module.get_air_temp_hum(sensor_id=-1))
        self.assertEqual(None, self.api_module.get_air_temp_hum(sensor_id=0))
        self.assertNotEqual(None, self.api_module.get_air_temp_hum(sensor_id=1))
        self.assertNotEqual(None, self.api_module.get_air_temp_hum(sensor_id=4))
        for i in range(1, 5):
            resp = self.api_module.get_air_temp_hum(sensor_id=i)
            self.assertEqual(i, resp.get('id'))
            self.assertIn('temperature', str(resp))
            self.assertIn('humidity', str(resp))

    def test_ground_sensor(self):
        self.assertEqual(None, self.api_module.get_ground_hum(sensor_id=-1))
        self.assertEqual(None, self.api_module.get_ground_hum(sensor_id=0))
        self.assertEqual(None, self.api_module.get_ground_hum(sensor_id=7))
        self.assertNotEqual(None, self.api_module.get_ground_hum(sensor_id=1))
        self.assertNotEqual(None, self.api_module.get_ground_hum(sensor_id=6))
        for i in range(1, 7):
            resp = self.api_module.get_ground_hum(sensor_id=i)
            self.assertEqual(i, resp.get('id'))
            self.assertIn('humidity', str(resp))

    def test_hydration_system(self):
        self.assertDictEqual({'code': 200, 'message': 'State success change. Hydration success start'},
                             self.api_module.control_humidity_system(state=1))
        self.assertDictEqual({'code': 200, 'message': 'State success change. Hydration success end'},
                             self.api_module.control_humidity_system(state=0))
        self.assertDictEqual({'code': 404, 'message': 'State value not found'},
                             self.api_module.patch(url='https://dt.miet.ru/ppo_it/api/total_hum',
                                                   params={
                                                       'state': str(-1)
                                                   }).json())
        self.assertDictEqual({'code': 404, 'message': 'State value not found'},
                             self.api_module.patch(url='https://dt.miet.ru/ppo_it/api/total_hum').json())
        self.assertEqual(None, self.api_module.control_humidity_system(state=-1))
        self.assertEqual(None, self.api_module.control_humidity_system(state=2))

    def test_window_system(self):
        self.assertDictEqual({'code': 200, 'message': 'State success change. Window success open'},
                             self.api_module.control_windows(state=1))
        self.assertDictEqual({'code': 200, 'message': 'State success change. Window success close'},
                             self.api_module.control_windows(state=0))
        self.assertDictEqual({'code': 404, 'message': 'State value not found'},
                             self.api_module.patch(url='https://dt.miet.ru/ppo_it/api/fork_drive',
                                           params={
                                               'state': str(-1)
                                           }).json())
        self.assertDictEqual({'code': 404, 'message': 'State value not found'},
                             self.api_module.patch(url='https://dt.miet.ru/ppo_it/api/fork_drive').json())
        self.assertEqual(None, self.api_module.control_windows(state=-1))
        self.assertEqual(None, self.api_module.control_windows(state=2))

    def test_control_watering(self):
        self.assertEqual(None, self.api_module.control_watering(pomp_id=0, state=-1))
        self.assertEqual(None, self.api_module.control_watering(pomp_id=1, state=-1))
        self.assertDictEqual({'code': 200, 'message': 'State success change. Watering success close'},
                             self.api_module.control_watering(pomp_id=1, state=0))
        self.assertEqual(None, self.api_module.control_watering(pomp_id=-1, state=1))
        for i in range(1, 7):
            self.assertDictEqual({'code': 200, 'message': 'State success change. Watering success open'},
                                 self.api_module.control_watering(pomp_id=i, state=1))
        for i in range(1, 7):
            self.assertDictEqual({'code': 200, 'message': 'State success change. Watering success close'},
                                 self.api_module.control_watering(pomp_id=i, state=0))
        self.assertDictEqual({'code': 404, 'message': 'State value or id not found'},
                             self.api_module.patch(url='https://dt.miet.ru/ppo_it/api/watering',
                                           params={
                                               'id': str(0),
                                               'state': str(-1)
                                           }).json())
        self.assertDictEqual({'code': 404, 'message': 'State value or id not found'},
                             self.api_module.patch(url='https://dt.miet.ru/ppo_it/api/watering',
                                           params={
                                               'id': str(3),
                                               'state': str(-1)
                                           }).json())
        self.assertDictEqual({'code': 404, 'message': 'State value or id not found'},
                             self.api_module.patch(url='https://dt.miet.ru/ppo_it/api/watering',
                                           params={
                                               'id': str(10),
                                               'state': str(-1)
                                           }).json())
        self.assertDictEqual({'code': 404, 'message': 'State value or id not found'},
                             self.api_module.patch(url='https://dt.miet.ru/ppo_it/api/watering',
                                           params={
                                               'id': str(10),
                                               'state': str(-1)
                                           }).json())
        self.assertDictEqual({'code': 404, 'message': 'State value or id not found'},
                             self.api_module.patch(url='https://dt.miet.ru/ppo_it/api/watering',
                                           params={
                                               'id': str(10),
                                               'state': str(0)
                                           }).json())
        self.assertDictEqual({'code': 404, 'message': 'State value or id not found'},
                             self.api_module.patch(url='https://dt.miet.ru/ppo_it/api/watering',
                                           params={
                                               'id': str(0),
                                               'state': str(1)
                                           }).json())
        self.assertDictEqual({'code': 404, 'message': 'State value or id not found'},
                             self.api_module.patch(url='https://dt.miet.ru/ppo_it/api/watering',
                                           params={
                                               'id': str(1),
                                               'state': str(10)
                                           }).json())
        self.assertDictEqual({'code': 404, 'message': 'State value not found'},
                             self.api_module.patch(url='https://dt.miet.ru/ppo_it/api/watering',
                                           params={
                                               'id': str(1)
                                           }).json())
        self.assertDictEqual({'code': 404, 'message': 'State value not found'},
                             self.api_module.patch(url='https://dt.miet.ru/ppo_it/api/watering',
                                           params={
                                               'state': str(10)
                                           }).json())


if __name__ == "__main__":
    unittest.main()
