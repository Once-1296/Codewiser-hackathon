class AppException(Exception):
    """
    Base application exception.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ValidationException(AppException):
    pass


class ServiceException(AppException):
    pass