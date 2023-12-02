from pydantic import BaseModel, BaseConfig


class BaseSchema(BaseModel):
    class Config(BaseConfig):
        from_attributes = True
        arbitrary_types_allowed = True


class ChatRoomInputSchema(BaseSchema):
    name: str
    description: str
    is_private: str


class ChatRoomResponseSchema(BaseSchema):
    name: str
    description: str
    is_private: str
    id: int
