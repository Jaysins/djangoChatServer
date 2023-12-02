from ninja import NinjaAPI
from authy.api import router as auth_router
from chat.api import router as chat_router
from core.middleware import JWTAuthenticationMiddleware
from djangoChatServer.exceptions import CustomValidationError

api = NinjaAPI(auth=JWTAuthenticationMiddleware())


@api.exception_handler(CustomValidationError)
def validation_failed(request, exc):
    return api.create_response(request, {"message": exc.message}, status=exc.status_code)


api.add_router("/", auth_router)
api.add_router("/", chat_router)
