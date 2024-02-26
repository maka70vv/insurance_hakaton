from django.contrib import admin

from medical_services.models import MedicalServices, VZRServices


class MedicalServicesAdmin(admin.ModelAdmin):
    search_fields = ['name']



class VZRAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(MedicalServices, MedicalServicesAdmin)
admin.site.register(VZRServices, VZRAdmin)