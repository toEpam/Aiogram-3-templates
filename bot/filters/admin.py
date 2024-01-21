from aiogram.filters import BaseFilter
from aiogram.types import Message
from icecream import ic

from bot.data.config import ADMINS


class AdminFilter(BaseFilter):
    is_admin: bool = True

    async def __call__(self, obj: Message) -> bool:
        # ic(ADMINS)
        # ic(obj.from_user.id)
        # ic(obj.from_user.id in ADMINS)
        # ic(self.is_admin)
        # ic(obj.from_user.id in ADMINS == self.is_admin)
        return (str(obj.from_user.id) in ADMINS) == self.is_admin
