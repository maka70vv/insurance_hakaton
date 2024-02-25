from django.db import models

from limts_by_user.models import LimitsByUser
from medical_services.models import MedicalServices, VZRServices
from users.models import User


class MedicalPaymentRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(MedicalServices, on_delete=models.CASCADE)
    limit = models.ForeignKey(LimitsByUser, on_delete=models.CASCADE)
    kkmCheck = models.FileField(upload_to='dms/kkm/')
    referral = models.FileField(upload_to='dms/napravleniya/', null=True, blank=True)
    invoice = models.FileField(upload_to='dms/schet-fakturi/', null=True, blank=True)
    opinions_on_medications = models.FileField(upload_to='dms/zaklucheniyaMedicamenty/', null=True, blank=True)
    sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dateTime = models.DateTimeField(null=True, blank=True)
    inn = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return self.dateTime

    class Meta:
        app_label = "payments"


class VZRPaymentRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(VZRServices, on_delete=models.CASCADE)
    limit = models.ForeignKey(LimitsByUser, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    summ = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    final_summ = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    medical_docs = models.FileField(upload_to='vzr/medical/')
    travel_docs = models.FileField(upload_to='vzr/travel/')
    invoice = models.FileField(upload_to='vzr/invoices/')
    approved = models.BooleanField(default=False)
    proposed = models.BooleanField(default=False)

    def __str__(self):
        return self.dateTime

    class Meta:
        app_label = "payments"
