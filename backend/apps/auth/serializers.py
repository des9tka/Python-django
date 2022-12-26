from rest_framework import serializers

from apps.users.models import UserModel


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('password',)