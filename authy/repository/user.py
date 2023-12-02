from authy.models import User
from core.repository import BaseRepository


class UserRepository(BaseRepository):
    model = User
