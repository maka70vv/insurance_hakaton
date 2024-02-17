from django.contrib import admin

from medical_services.models import MedicalServies


class MedicalServiesAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(MedicalServies, MedicalServiesAdmin)
