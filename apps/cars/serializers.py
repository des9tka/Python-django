from rest_framework.serializers import ModelSerializer

from apps.cars.models import CarModel


class CarsSerializer(ModelSerializer):

    class Meta:
        model = CarModel
        # fields = '__all__'
        exclude = ('auto_park',)