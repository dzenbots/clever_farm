from aiogram.dispatcher.filters.state import StatesGroup, State


class SetParamsStates(StatesGroup):
    set_request_timeout = State()
    set_min_air_temp = State()
    set_max_air_temp = State()
    set_min_air_hum = State()
    set_max_air_hum = State()
    set_min_ground_hum = State()
    set_max_ground_hum = State()
