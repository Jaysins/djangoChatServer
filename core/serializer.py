from pydantic import BaseModel, BaseConfig


class BaseSchema(BaseModel):
    class Config(BaseConfig):
        from_attributes = True

