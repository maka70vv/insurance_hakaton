from django.contrib import admin

from tariffs.models import Tariff


class TariffAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Tariff, TariffAdmin)
