from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async
import jwt


class ChannelJWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        # Extract the JWT token from the WebSocket connection scope
        jwt_token = self.get_jwt_token_from_scope(scope)
        if not jwt_token:
            return None
        # Validate the JWT token
        validated_token = await self.validate_jwt_token(jwt_token)
        # If the token is valid, associate the user with the WebSocket connection
        scope['user'] = await self.get_user_from_token(validated_token)

        return await super().__call__(scope, receive, send)

    def get_jwt_token_from_scope(self, scope):
        # Extract the JWT token from the scope (e.g., from query string or headers)
        # Implement logic to retrieve the token from the WebSocket scope
        print(self)
        print('oa, scorm', scope)
        headers = scope.get("headers")
        print(headers)
        auth_header = [value[1] for value in headers if value[0].decode() == 'authorization']
        if not auth_header:
            return

        auth_header = auth_header[0].decode().split()

        if len(auth_header) < 2:
            return

        return auth_header[1]

    @database_sync_to_async
    def validate_jwt_token(self, token):
        # Validate the JWT token (using rest_framework_simplejwt or your JWT library)
        from django.conf import settings
        try:
            print('ia m token', token, type(token))
            validated_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
            return validated_token
        except Exception as e:
            raise e

    @database_sync_to_async
    def get_user_from_token(self, validated_token):
        from authy.services.user import UserService
        # Get user information from the validated JWT token
        user = validated_token.get('id')
        return UserService.get_by_id(int(user))
