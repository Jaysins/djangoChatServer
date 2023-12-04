from channels.db import database_sync_to_async

from ..repository.message import MessageRepository
from core.service import BaseService


class MessageService(BaseService):
    repository = MessageRepository

    @classmethod
    @database_sync_to_async
    def log_message(cls, room, user, message: dict, **kwargs):
        """
        Method to join a user to a chat room.
        """
        message = f"{user.username}: {message.get('content')}"
        cls.create(**{"chat_room": room, "user": user, "content": message})
        return message
