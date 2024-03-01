from django.db import models

from insurance_companies.models import Company
# Create your models here.

class Analytica(models.Model):
    commission = models.PositiveIntegerField()
    sales_amount = models.PositiveIntegerField()
    purchase_amount = models.PositiveIntegerField()
    insurance_company = models.ForeignKey(Company, on_delete=models.CASCADE)
