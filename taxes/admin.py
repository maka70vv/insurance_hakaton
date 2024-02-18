from django.contrib import admin

from taxes.models import TaxTips


@admin.register(TaxTips)
class TaxesAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'percent']
