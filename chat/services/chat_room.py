from channels.db import database_sync_to_async

from ..repository.chat_room import ChatRoomRepository
from core.service import BaseService


class ChatRoomService(BaseService):
    repository = ChatRoomRepository

    @classmethod
    @database_sync_to_async
    def join_room(cls, obj_id: int, user, **kwargs):
        """
        Method to join a user to a chat room.
        """

        room = cls.get_by_id(obj_id)
        room.participants.add(user)
        return room

    @classmethod
    @database_sync_to_async
    def leave_room(cls, obj_id: int, user, **kwargs):
        """
        Method to remove a user from a chat room.
        """

        room = cls.get_by_id(obj_id)
        room.participants.remove(user)
        return {"status": "success"}

    @classmethod
    @database_sync_to_async
    def a_get_by_id(cls, obj_id: int, **kwargs):
        """
        Method to remove a user from a chat room.
        """

        return cls.get_by_id(obj_id)

    @classmethod
    def get_room_participants(cls, obj_id: int, **kwargs):
        """
        Method to get participants of a chat room.
        """

        room = cls.get_by_id(obj_id)
        return room.participants.all()  # Returns all participants of the chat room

    @classmethod
    def get_room_messages(cls, obj_id: int, **kwargs):
        """
        Method to get messages of a chat room.
        """

        room = cls.get_by_id(obj_id)
        return room.messages.all()  # Returns all participants of the chat room
