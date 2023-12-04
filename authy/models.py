from core.model import *
from datetime import datetime, timedelta
from django.conf import settings
import jwt


class User(BaseModel):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.email  # Customize how the object is displayed in admin or shell

    def generate_token(self):
        """ Generate the auth token for this user from the current data embedded within the application """

        if not self.id:
            raise ValueError("Cannot generate token for unsaved object")

        expires_in = datetime.now() + timedelta(hours=int(settings.JWT_EXPIRES_IN_HOURS))

        payload = dict(name=self.username, id=str(self.id), exp=expires_in)
        print(settings.JWT_SECRET_KEY)
        # print(payload, "token the payload")
        encoded = jwt.encode(payload, key=settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return encoded
