from django.db import models


class TaxTips(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название налога")
    percent = models.PositiveIntegerField(verbose_name="Налоговая ставка (в %)")

    def __str__(self):
        return self.name
