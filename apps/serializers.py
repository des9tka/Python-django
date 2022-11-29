from rest_framework import serializers

from apps.users.models import CarModel


class CarsSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    car_brand = serializers.CharField(max_length=255)
    year_release = serializers.IntegerField()
    seats_number = serializers.IntegerField()
    body_type = serializers.CharField(max_length=255)
    engine_volume = serializers.FloatField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        return CarModel.objects.create(**validated_data)

