from core.enums.error_enums import ErrorEnum
from core.exceptions.jwt_exceptions import JWTException

from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_error_handler(exc: Exception, context: dict) -> Response:
    handlers = {
        'JWTException': _jwt_validate_error
    }

    response = exception_handler(exc, context)
    exc_class = exc.__class__.__name__

    if exc_class in handlers:
        return handlers[exc_class](exc, context)

    return response


def _jwt_validate_error(exc: JWTException, content: dict) -> Response:
    return Response(ErrorEnum.JWT.massage, ErrorEnum.JWT.code)
