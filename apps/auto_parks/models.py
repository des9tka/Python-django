from django.db import models

from apps.users.models import UserModel


class AutoParksModel(models.Model):
    class Meta:
        db_table = 'auto_parks'

    name = models.CharField(max_length=20)
    users = models.ManyToManyField(UserModel, through='UsersAutoParksModel', related_name='auto_parks')


class UsersAutoParksModel(models.Model):
    class Meta:
        db_table = 'cars_auto_parks'

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    auto_parks = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE)
