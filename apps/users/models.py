from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
    car_brand = models.CharField(max_length=255)
    year_release = models.IntegerField()
    seats_number = models.IntegerField()
    body_type = models.CharField(max_length=255)
    engine_volume = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

