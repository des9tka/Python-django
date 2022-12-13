import os
from uuid import uuid1


def upload_cars_photo(instance, file: str) -> str:
    extension = file.split('.')[-1]
    return os.path.join("cars", f'{instance.car.id}', 'photo', f'{uuid1()}.{extension}')
