# Работа с API умной теплицы

## Описание реализованных методов

Для реализации функций запросов к API умной теплицы был написан класс 
```FarmApiModule```, унаследованный от класса ```Session``` из библиотеки 
```requests```. В данном классе реализованы запросы к API умной теплицы 
отдельными методами с передачей нужных аргументов. Приведем пример методов,
реализующих ```GET``` и ```POST``` запросы к API теплицы:
```python
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
```

На вход функции получают необходмые параметры, происходит проверка 
корректности входных параметров, формирование и передача запроса и, в случае 
успеха, возвращается ответ для дальнейшей обработки.

Полный код класса ```FarmApiModule``` можно посмотреть в файле 
[api_module.py](../farm_api_module/api_module.py).
