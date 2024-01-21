from aiogram.filters import BaseFilter
from aiogram.types import Message

from bot.data.config import ADMINS


class AdminFilter(BaseFilter):
    is_admin: bool = True

    async def __call__(self, obj: Message) -> bool:
        return (obj.from_user.id in ADMINS) == self.is_admin
