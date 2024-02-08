from django.db import models

from insurance_industry.models import Industry
from tariffs.models import Tariff


class Limit(models.Model):
    limitName = models.CharField(max_length=150)
    limitSumm = models.PositiveIntegerField(default=0)
    verboseIndustry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    verboseTariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)
