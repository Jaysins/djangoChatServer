import jwt
from django.conf import settings
from ninja.security import HttpBearer


class JWTAuthenticationMiddleware(HttpBearer):

    def authenticate(self, request, token):
        from authy.services.user import UserService
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return
        auth_header = auth_header.split()
        if len(auth_header) < 2:
            return

        payload = jwt.decode(auth_header[1], settings.JWT_SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("id")
        if not user_id:
            return None
        request.user = UserService.get_by_id(int(user_id))
        return int(user_id)
