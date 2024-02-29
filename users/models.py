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
    date_of_birth = models.DateTimeField(blank=True, null=True)
    passport_number = models.CharField(max_length=9, blank=True)
    date_of_issue = models.DateTimeField(blank=True, null=True)
    date_expiration = models.DateTimeField(blank=True, null=True)
    authority = models.CharField(max_length=10, blank=True)
    sex = models.CharField(
        max_length=10,
        blank=True, null=True,
        choices=[
            ("male", "мужской"),
            ("female", "женский"),
        ],
    )
    place_of_birth = models.CharField(max_length=50, blank=True)
    place_of_residence = models.TextField(blank=True, null=True)
    residential_addres = models.TextField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to="profile_photos", blank=True, null=True)

    # Fields for juridical persons
    fullname = models.CharField(max_length=255, blank=True, null=True)
    okpo = models.CharField(max_length=25, blank=True, null=True)
    registration_number = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    ceo = models.CharField(max_length=255, blank=True, null=True)
    position_of_ceo = models.CharField(max_length=255, blank=True, null=True)
    envoy = models.CharField(max_length=255, blank=True, null=True)
    legal_address = models.CharField(max_length=500, blank=True, null=True)
    actual_address = models.CharField(max_length=500, blank=True, null=True)


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
