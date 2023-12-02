from ninja import Router

from djangoChatServer.exceptions import CustomValidationError
from .serializers import UserSignupInput, UserResponseSchema, UserLoginInput
from .services.user import UserService

router = Router()


@router.post("/signup/", response=UserResponseSchema, auth=None)
def signup(request, user_data: UserSignupInput):
    # Check if the email already exists in the UserRepository

    if UserService.find_one(email=user_data.email):
        raise CustomValidationError(message="User with this email already exists")

    user_data = user_data.model_dump()
    user_data["username"] = user_data.get("username").lower()
    user_data["email"] = user_data.get("email").lower()
    # Create the user
    created_user = UserService.register(**user_data)
    # Return the created user object upon successful signup (excluding password)
    created_user.auth_token = created_user.generate_token()
    return created_user


@router.post("/login/", response=UserResponseSchema, auth=None)
def login(request, user_data: UserLoginInput):
    # Check if the email already exists in the UserRepository

    if not UserService.find_one(email=user_data.email.lower()):
        raise CustomValidationError(message="User with this email does not exist")

    user_data = user_data.model_dump()
    user_data["email"] = user_data.get("email").lower()
    # authenticate the user
    user = UserService.authenticate_user(**user_data)
    if not user:
        raise CustomValidationError(message="User with this email already exists")
    # Return the created user object upon successful signup (excluding password)
    user.auth_token = user.generate_token()
    return user
