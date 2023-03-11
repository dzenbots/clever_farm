from aiogram.dispatcher.filters import Command


class CommandAirTemp(Command):
    def __init__(self):
        super().__init__(['airtemp'])


class CommandAirHum(Command):
    def __init__(self):
        super().__init__(['airhum'])


class CommandGroundHum(Command):
    def __init__(self):
        super().__init__(['groundhum'])


class CommandControl(Command):
    def __init__(self):
        super().__init__(['control'])


class CommandAddValues(Command):
    def __init__(self):
        super().__init__(['add_values'])


class CommandForceControl(Command):
    def __init__(self):
        super().__init__(['force_control'])


class CommandSetParams(Command):
    def __init__(self):
        super().__init__(['set_params'])
