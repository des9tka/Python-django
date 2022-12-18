from enum import Enum

from rest_framework import status


class ErrorEnum(Enum):
    JWT = (
        {'details': 'Token is invalid or expired'},
        status.HTTP_400_BAD_REQUEST
    )

    def __init__(self, massage: dict, code=status.HTTP_400_BAD_REQUEST):
        self.massage = massage
        self.code = code
