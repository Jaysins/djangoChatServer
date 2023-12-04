from typing import List

from core.serializer import *
from authy.serializers import UserResponseSchema


class BaseSchema(BaseModel):
    class Config(BaseConfig):
        from_attributes = True


class DefaultResponseSchema(BaseSchema):
    status: str


class ChatRoomInputSchema(BaseSchema):
    name: str
    description: str
    is_private: bool = False
    max_participants: int = None


class JoinChatRoomInputSchema(BaseSchema):
    action: str


class ChatRoomUpdateSchema(BaseSchema):
    name: str = None
    description: str = None
    is_private: bool = False
    max_participants: int = None


class ChatRoomResponseSchema(BaseSchema):
    name: str
    description: str
    is_private: bool
    id: int
    user: UserResponseSchema
