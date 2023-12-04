from ..models import Message
from core.repository import BaseRepository


class MessageRepository(BaseRepository):
    model = Message
