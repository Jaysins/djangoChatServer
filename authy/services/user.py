import bcrypt

from authy.repository.user import UserRepository
from core.service import BaseService


class UserService(BaseService):
    repository = UserRepository

    @classmethod
    def register(cls, **kwargs):
        """

        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        password = kwargs.pop('password')
        password = (bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())).decode()
        kwargs["password"] = password
        user = cls.repository.create(kwargs)
        return user

    @classmethod
    def authenticate_user(cls, email: str, password: str):
        """

        :param email:
        :type email:
        :param password:
        :type password:
        :return:
        :rtype:
        """

        user = cls.repository.find_one(email=email)
        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return None
        return user
