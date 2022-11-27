import json

from rest_framework.views import APIView
from rest_framework.response import Response


class FileReadWriteService:
    _file_name = None

    @classmethod
    def get_users(cls):
        try:
            with open(cls._file_name) as file:
                return json.load(file)
        except (Exception,):
            return []

    @classmethod
    def save_users(cls, data):
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

    def post(self, *args, **kwargs):
        data = self.request.data
        data['id'] = self.users[-1]['id'] + 1 if self.users else 1
        self.users.append(data)
        self.save_users(self.users)
        return Response(data)


class UserGetUpdateDeleteView(CustomAPIView):

    def _get_user_by_id(self, pk):
        try:
            user = next((user for user in self.users if user['id'] == pk))
            return user
        except (Exception,):
            return 'Not found'

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        return Response(self._get_user_by_id(pk))

    def put(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs.get('pk')
        user = self._get_user_by_id(pk)
        if data.get('id'):
            del data['id']
        user |= data
        self.save_users(self.users)
        return Response(data)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        index = next((i for i, v in enumerate(self.users) if v['id'] == pk), None)

        if index is None:
            return Response('Not Found')

        del self.users[index]
        self.save_users(self.users)
        return Response('deleted')