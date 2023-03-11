from aiogram.dispatcher.filters.state import StatesGroup, State


class AddValuesStates(StatesGroup):
    wait_for_air_temp_values = State()
    wait_for_air_hum_values = State()
    wait_for_ground_hum_values = State()
