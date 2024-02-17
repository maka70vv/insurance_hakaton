from django.contrib import admin

from insurance_industry.models import Industry


class IndustryAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Industry, IndustryAdmin)
