from django.db import models


class Tariff(models.Model):
    name = models.CharField(max_length=40)
