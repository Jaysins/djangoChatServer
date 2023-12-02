from ninja.errors import HttpError


class CustomValidationError(HttpError):
    def __init__(self, message):
        self.message = message
        super().__init__(status_code=409, message=message)
