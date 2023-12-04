from ..repository.chat_room import ChatRoomRepository
from core.service import BaseService

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class ChatRoomService(BaseService):
    repository = ChatRoomRepository

    @classmethod
    def join_room(cls, obj_id: int, user, **kwargs):
        """
        Method to join a user to a chat room.
        """

        room = cls.get_by_id(obj_id)
        room.participants.add(user)
        return room

    @classmethod
    def leave_room(cls, obj_id: int, user, **kwargs):
        """
        Method to remove a user from a chat room.
        """

        room = cls.get_by_id(obj_id)
        room.participants.remove(user)
        return {"status": "success"}

    @classmethod
    def get_room_participants(cls, obj_id: int, **kwargs):
        """
        Method to get participants of a chat room.
        """

        room = cls.get_by_id(obj_id)
        return room.participants.all()  # Returns all participants of the chat room
