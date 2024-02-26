from django.contrib import admin

from payments.models import MedicalPaymentRequest, VZRPaymentRequest, GruzPaymentRequest


class PaymentAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__first_name', 'dateTime']
    list_filter = ['dateTime']


admin.site.register(MedicalPaymentRequest, PaymentAdmin)
admin.site.register(VZRPaymentRequest, PaymentAdmin)
admin.site.register(GruzPaymentRequest, PaymentAdmin)
