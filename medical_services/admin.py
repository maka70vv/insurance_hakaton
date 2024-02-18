from django.contrib import admin

from medical_services.models import MedicalServies, VZRServices


class MedicalServiesAdmin(admin.ModelAdmin):
    search_fields = ['name']



class VZRAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(MedicalServies, MedicalServiesAdmin)
admin.site.register(VZRServices, VZRAdmin)
