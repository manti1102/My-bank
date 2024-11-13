from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from users.managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):

    username = None
    phone_number = models.CharField(
        max_length=25,
        validators=[MinLengthValidator(6)],
        unique=True,
    )
    balance = models.PositiveBigIntegerField(default=0)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'