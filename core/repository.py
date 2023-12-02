from contextlib import contextmanager
from core.utils import populate_obj


class BaseRepository:
    model = None
    
    @classmethod
    def create(cls, entity):
        return cls.model.objects.create(**entity)
    
    @classmethod
    def filter(cls, **kwargs):
        """
        Perform filtering on User objects based on given criteria.
        Example: AuthRepository.filter(username='example')
        """
        return cls.model.objects.filter(**kwargs)
    
    @classmethod
    def find_one(cls, **kwargs):
        """
        Return a single User object based on given criteria.
        Example: AuthRepository.find_one(username='example')
        """
        return cls.filter(**kwargs).first()
    
    @classmethod
    def get_by_id(cls, obj_id):
        """
        Retrieve a User object by ID.
        Example: AuthRepository.get_by_id(1)
        """

        try:
            obj = cls.model.objects.get(id=obj_id)
            return obj
        except cls.model.DoesNotExist:
            return None
        
    @classmethod
    def update(cls, obj_id, **kwargs):
        """
        Update a User object based on the given ID and provided data.
        Example: AuthRepository.update(1, username='new_username')
        """
        obj = cls.get_by_id(obj_id)
        if not obj:
            return
        obj = populate_obj(obj, kwargs)
        return obj.save()
    
    @classmethod
    def delete(cls, user_id):
        """
        Delete a User object by ID.
        Example: AuthRepository.delete(1)
        """
        user = cls.get_by_id(user_id)
        user.delete()
        return True
