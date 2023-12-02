from ..repository.chat_room import ChatRoomRepository
from core.service import BaseService


class ChatRoomService(BaseService):
    repository = ChatRoomRepository
