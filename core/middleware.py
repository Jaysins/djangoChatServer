from ninja.security import APIKeyCookie
import jwt
from django.conf import settings


class JWTAuthenticationMiddleware(APIKeyCookie):
    def authenticate(self, request, token):

        payload = jwt.decode(request.headers.get("Authorization"), settings.JWT_SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("id")
        if not user_id:
            return None
        request.user = payload
        return int(user_id)
