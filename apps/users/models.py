from django.db import models

from apps.auto_parks.models import AutoParksModel


class CarModel(models.Model):
    class Meta:
        db_table = 'users'

    car_brand = models.CharField(max_length=255)
    year_release = models.IntegerField()
    seats_number = models.IntegerField()
    body_type = models.CharField(max_length=255)
    engine_volume = models.FloatField()
    auto_park = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
