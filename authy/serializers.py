from core.serializer import *


class UserSignupInput(BaseSchema):
    email: str
    username: str
    phone: str
    password: str


class UserLoginInput(BaseSchema):
    email: str
    password: str


class UserResponseSchema(BaseSchema):
    email: str
    id: int
    username: str


class AuthResponseSchema(UserResponseSchema):
    auth_token: str
