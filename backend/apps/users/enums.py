from enum import Enum


class RegEx(Enum):
    PASSWORD = (
         r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\s])[^\s]{8,20}$',
        [
            'password must have one number (0-9)',
            'password must have one upperCase letter',
            'password must have one lowerCase letter',
            'password must have one specialChar',
            'password must have min = 8, max = 20 chars',
        ]
    )

    NAME = (
        r'^[a-zA-Z]{2,20}$',
        [
            'name must contain only letters',
            'min = 2, max = 20'
        ]
    )

    SURNAME = (
        r'^[a-zA-Z]{2,30}$',
        [
            'surname must contain only letters',
            'min = 2, max = 30'
        ]
    )

    PHONE = (
        r'^0[95687]\d{8}$',
        [
            'invalid phone number',
            'phone number must contain 10 numbers, first - "0"'
        ]
    )

    def __init__(self, pattern, massage: str | list[str]):
        self.pattern = pattern
        self.massage = massage
