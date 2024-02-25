from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


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


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date_of_birth = models.DateTimeField(blank=True, null=True)
    passport_number = models.CharField(max_length=9, blank=True)
    date_of_issue = models.DateTimeField(blank=True, null=True)
    date_expiration = models.DateTimeField(blank=True, null=True)
    authority = models.CharField(max_length=10, blank=True)
    sex = models.CharField(
        max_length=10,
        choices=[
            ("male", "мужской"),
            ("female", "женский"),
        ],
    )
    place_of_birth = models.CharField(max_length=50, blank=True)
    place_of_residence = models.TextField(blank=True, null=True)
    residential_addres = models.TextField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to="profile_photos", blank=True)
