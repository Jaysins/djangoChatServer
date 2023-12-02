from ninja import NinjaAPI
from authy.api import router as auth_router
from djangoChatServer.exceptions import CustomValidationError

api = NinjaAPI()


@api.exception_handler(CustomValidationError)
def validation_failed(request, exc):
    return api.create_response(request, {"message": exc.message}, status=exc.status_code)


api.add_router("/", auth_router)
