from django.db import models


class DamagePaymentsRange(models.Model):
    min_damage = models.PositiveSmallIntegerField(default=0, verbose_name="Минимальный порог для суммы (% повреждения)")
    max_damage = models.PositiveSmallIntegerField(default=1, verbose_name="Максимальный порог для суммы (% повреждения)")
    payment_summ = models.IntegerField(default=0, verbose_name="Сумма в диапазоне")

    def __str__(self):
        return self.max_damage
