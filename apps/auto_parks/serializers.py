from rest_framework.serializers import ModelSerializer

from .models import AutoParksModel
from apps.cars.serializers import CarsSerializer


class AutoParksSerializer(ModelSerializer):
    cars = CarsSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParksModel
        fields = '__all__'
