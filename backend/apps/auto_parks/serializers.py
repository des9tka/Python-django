from rest_framework.serializers import ModelSerializer

from apps.cars.serializers import CarsSerializer

from .models import AutoParksModel


class AutoParksSerializer(ModelSerializer):
    cars = CarsSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParksModel
        fields = ('id', 'name', 'cars', 'users')
        depth = 1
