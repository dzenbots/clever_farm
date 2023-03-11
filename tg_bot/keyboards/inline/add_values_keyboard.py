from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

add_values_callback_data = CallbackData('add_values', 'param')

add_values_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Температура и влажность воздуха',
                callback_data=add_values_callback_data.new(
                    param='temp_hum'
                )
            )
        ],
        [
            InlineKeyboardButton(
                text='Влажность почвы',
                callback_data=add_values_callback_data.new(
                    param='ground_hum'
                )
            )
        ]
    ]
)
