from django.contrib import admin

from insurance_companies.models import Company


@admin.register(Company)
class InsuranceCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn')
    search_fields = 'name'
