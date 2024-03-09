from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatTypeFilter(BaseFilter):  # [1]
    async def __call__(self, message: Message) -> bool:  # [3]
        return message.chat.type == "private"
