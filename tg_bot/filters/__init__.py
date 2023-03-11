from ..loader import dp
from .commands import CommandAirTemp, CommandControl, CommandAirHum, CommandGroundHum, CommandAddValues, \
    CommandForceControl, CommandSetParams
from .role_filter import RoleFilter

if __name__ == "tg_bot.filters":
    dp.filters_factory.bind(RoleFilter)
    pass

__all__ = [CommandAirTemp, CommandControl, CommandAirHum, CommandGroundHum, RoleFilter, CommandAddValues,
           CommandForceControl, CommandSetParams, dp]
