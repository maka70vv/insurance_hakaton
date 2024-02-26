from django.db import models


class MedicalServices(models.Model):
    name = models.CharField(max_length=100)
    verboseLimitName = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class VZRServices(models.Model):
    name = models.CharField(max_length=100)
    verboseLimitName = models.CharField(max_length=100)

    def __str__(self):
        return self.name