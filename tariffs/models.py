from django.db import models

from insurance_companies.models import Company
from insurance_industry.models import Industry


class Tariff(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class PricesByCompany(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()
    verbose_industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

    def __str__(self):
        return self.company.name
