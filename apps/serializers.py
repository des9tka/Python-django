from rest_framework.serializers import ModelSerializer
from apps.users.models import CarModel


class CarsSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

