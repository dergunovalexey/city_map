from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    phone = models.CharField(max_length=11, verbose_name="Номер телефона",
                             validators=[
                                 RegexValidator('+\d{10}',
                                                message="Неверный номер")
                                 ])
