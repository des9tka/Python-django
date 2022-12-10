from abc import ABC, abstractmethod

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.auto_parks.serializers import AutoParksSerializer

from .models import UserModel
from .permissions import IsSuperUser
from .serializers import UserSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)


class AdminTools(GenericAPIView, ABC):
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.id)

    @abstractmethod
    def patch(self, *args, **kwargs):
        pass


class SuperUserTools(AdminTools, ABC):
    permission_classes = (IsSuperUser,)


class UserActivateView(AdminTools):
    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDeactivateView(AdminTools):
    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_active:
            user.is_active = False
            user.save()
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)


class UserToAdminView(SuperUserTools):
    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(SuperUserTools):
    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_staff:
            user.is_staff = False
            user.save()
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)


class AutoParksListCreateView(GenericAPIView):
    def get_object(self) -> UserModel:
        return self.request.user

    def get(self, *args, **kwargs):
        auto_parks = self.get_object().auto_parks
        serializer = AutoParksSerializer(auto_parks, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = AutoParksSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = self.get_object()
        serializer.save(user=user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


        
