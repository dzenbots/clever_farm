from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

set_params_callback = CallbackData('set_params', 'param', 'arg')

set_params_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='⬇️ Температура воздуха ⬇️',
                callback_data=set_params_callback.new(
                    param='no_param',
                    arg='no_arg'
                )
            )
        ],
        [
            InlineKeyboardButton(
                text='Минимальная',
                callback_data=set_params_callback.new(
                    param='air_temp',
                    arg='min'
                )
            ),
            InlineKeyboardButton(
                text='Максимальная',
                callback_data=set_params_callback.new(
                    param='air_temp',
                    arg='max'
                )
            )
        ],
        [
            InlineKeyboardButton(
                text='⬇️ Влажность воздуха ⬇️',
                callback_data=set_params_callback.new(
                    param='no_param',
                    arg='no_arg'
                )
            )
        ],
        [
            InlineKeyboardButton(
                text='Минимальная',
                callback_data=set_params_callback.new(
                    param='air_hum',
                    arg='min'
                )
            ),
            InlineKeyboardButton(
                text='Максимальная',
                callback_data=set_params_callback.new(
                    param='air_hum',
                    arg='max'
                )
            )
        ],
        [
            InlineKeyboardButton(
                text='⬇️ Влажность почвы ⬇️',
                callback_data=set_params_callback.new(
                    param='no_param',
                    arg='no_arg'
                )
            )
        ],
        [
            InlineKeyboardButton(
                text='Минимальная',
                callback_data=set_params_callback.new(
                    param='ground_hum',
                    arg='min'
                )
            ),
            InlineKeyboardButton(
                text='Максимальная',
                callback_data=set_params_callback.new(
                    param='ground_hum',
                    arg='max'
                )
            )
        ],
        [
            InlineKeyboardButton(
                text='Периодичность запросов',
                callback_data=set_params_callback.new(
                    param='request_timeout',
                    arg='no_arg'
                )
            )
        ],
    ]
)
