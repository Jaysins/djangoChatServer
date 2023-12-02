from pydantic import BaseModel, BaseConfig


class BaseSchema(BaseModel):
    class Config(BaseConfig):
        from_attributes = True


class UserSignupInput(BaseSchema):
    email: str
    username: str
    phone: str
    password: str


class UserLoginInput(BaseSchema):
    email: str
    password: str


class UserResponseSchema(BaseSchema):
    auth_token: str
    email: str
    id: int
    username: str
