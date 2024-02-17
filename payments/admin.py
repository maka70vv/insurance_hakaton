from django.contrib import admin

from payments.models import MedicalPaymentRequest


class PaymentAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__first_name', 'dateTime']


admin.site.register(MedicalPaymentRequest, PaymentAdmin)
