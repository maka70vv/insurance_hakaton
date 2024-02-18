from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    inn = models.CharField(
        max_length=14,
        unique=True,
        null=True,
        blank=True,
        verbose_name="ИИН",
    )
    iban_number = models.CharField(
        max_length=34,
        null=True,
        blank=True,
        verbose_name="Номер счета",
    )
