from django.db import models

from insurance_companies.models import Company
from insurance_industry.models import Industry


class Tariff(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
