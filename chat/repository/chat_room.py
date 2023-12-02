from ..models import Chatroom
from core.repository import BaseRepository


class ChatRoomRepository(BaseRepository):
    model = Chatroom
