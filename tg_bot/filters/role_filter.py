import typing
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery

from data import ADMINS


class RoleFilter(BoundFilter):
    key = 'role_filter'

    def __init__(self, role_filter: typing.Optional[str] = None):
        self.role_filter = role_filter

    async def check(self, obj):
        if self.role_filter is None:
            return
        if isinstance(obj, Message):
            if self.role_filter == 'admin':
                return str(obj.chat.id) in ADMINS
        if isinstance(obj, CallbackQuery):
            if self.role_filter == 'admin':
                return str(obj.message.chat.id) in ADMINS
        return False
