from django.db import models


class MedicalServies(models.Model):
    name = models.CharField(max_length=100)
    verboseLimitName = models.CharField(max_length=100)
