from rest_framework.views import APIView
from rest_framework.response import Response

users = [
    {"name":"Max", "age":15},
    {"name":"Oleg", "age":35},
    {"name":"Vanya", "age":20},
    {"name":"Kira", "age":30},
    {"name":"Andrey", "age":25}
]

class UserListView(APIView):
    def get(self, *args, **kwargs):
        return Response(users)

    def post(self, *args, **kwargs):
        new_user = self.request.data
        users.append(new_user)
        return Response(new_user)

class UserRetrieveUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            user = users[pk]
        except (Exception,):
            return Response('not found')
        return Response(user)

    def patch(self, *args, **kwargs):
        new_user = self.request.data
        pk = kwargs.get('pk')
        try:
            user = users[pk]
        except (Exception, ):
            return Response('not found user')
