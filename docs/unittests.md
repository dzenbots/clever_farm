# Unit-тестирование

## Что такое Unit-тестирование, описание модуля unittest и класса TestCase

## Созданные тесты

Для тестирования кода, реализующего запросы к API теплицы, был написан класс
```BasicModuleTest```, унаследованный от класса ```TestCase``` из модуля ```unittest```. 
Исходный код класса находится в файле 
[farm_api_module_tests.py](../tests/farm_api_module_tests.py).
Для примера, рассмотрим тестирование получение температуры и влажности воздуха:

В данном тесте сначала проверяется, что при передаче некорректных входных данных функция 
```api_module.get_air_temp_hum(...)``` возвращает None, как и следует из реализации 
данной функции в модуле [```farm_api_module```](../farm_api_module):
```python
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
```

После чего циклом происходит проверка получения информации от каждого из датчиков и корректность полученной информации.

Приведем еще пример - тестирование функции, реализующей запрос ```PATCH```:

```python
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
```
В данном тесте проверяется информация, полученная в ответе на запрос. 
Все запросы получают ```response.status_code=200```, но при передаче 
некорректных параметров в ответе присылается ```'code': 404``` с соответствующим 
сообщением. Это и проверяется в тесте - корректные ответы при корректных входных данных
и некорректные ответы при некорректных входных данных.

## Результат запуска всех тестов

```shell
Testing started at 17:52 ...
Launching unittests with arguments python -m unittest ../clever_farm/tests/farm_api_module_tests.py in ../clever_farm/tests


Ran 5 tests in 3.790s

OK
```

