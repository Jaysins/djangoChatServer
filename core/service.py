class BaseService:
    repository = None

    @classmethod
    def create(cls, **kwargs):
        return cls.repository.create(kwargs)

    @classmethod
    def filter(cls, **kwargs):
        """

        :param query:
        :type query:
        :return:
        :rtype:
        """
        return cls.repository.filter(**kwargs)

    @classmethod
    def find_one(cls, **kwargs):
        """

        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        return cls.repository.find_one(**kwargs)

    @classmethod
    def get_by_id(cls, obj_id):
        return cls.repository.get_by_id(obj_id)

    @classmethod
    def update_user(cls, obj_id, **kwargs):
        return cls.repository.update(obj_id, kwargs)

    @classmethod
    def delete_user(cls, obj_id):
        return cls.repository.delete(obj_id)
