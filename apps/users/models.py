from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from .enums import RegEx
from .managers import UserManager
from .services import upload_userAvatar


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[
        V.RegexValidator(RegEx.PASSWORD.pattern, RegEx.PASSWORD.massage)
    ])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

class ProfileModel(models.Model):
    class Meta:
        db_table = 'profiles'

    name = models.CharField(max_length=20, validators=[
        V.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.massage)
    ])
    surname = models.CharField(max_length=30, validators=[
        V.RegexValidator(RegEx.SURNAME.pattern, RegEx.SURNAME.massage)
    ])
    age = models.IntegerField(validators=[
        V.MinValueValidator(18), V.MaxValueValidator(150)
    ])
    phone = models.CharField(max_length=10, validators=[
        V.RegexValidator(RegEx.PHONE.pattern, RegEx.PHONE.massage)
    ])

    avatar = models.ImageField(upload_to=upload_userAvatar, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')

