from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer


