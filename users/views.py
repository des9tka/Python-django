import json

from rest_framework.views import APIView
from rest_framework.response import Response

import users


class FileReadWriteService:
    _file_name = None

    @classmethod
    def get_users(cls):
        try:
            with open(cls._file_name) as file:
                print(json.load(file))
                return json.load(file)
        except (Exception,):
            return []

    @classmethod
    def add_user(cls, data):
        try:
            with open(cls._file_name, mode='w') as file:
                json.dump(data, file)
        except Exception as err:
            str(err)


class CustomAPIView(APIView, FileReadWriteService):
    _file_name = 'users.json'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.users = self.get_users()


class UsersReadWriteView(CustomAPIView):
    def get(self, *args, **kwargs):
        return Response(self.users)

    def put(self, *args, **kwargs):
        data = self.request.data
        data['id'] = self.users[-1]['id']+1 if self.users else 1
        self.add_user(self.users)
        return Response(data)









