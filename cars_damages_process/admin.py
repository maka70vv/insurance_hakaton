from django.contrib import admin

from cars_damages_process.models import DamagePaymentsRange


@admin.register(DamagePaymentsRange)
class DamagePaymentsRangeAdmin(admin):
    list_display = ('min_damage', 'max_damage', 'payment_summ')