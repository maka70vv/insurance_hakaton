from django.db import models

from limts_by_user.models import LimitsByUser
from medical_services.models import MedicalServies
from users.models import User


class MedicalPaymentRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(MedicalServies, on_delete=models.CASCADE)
    limit = models.ForeignKey(LimitsByUser, on_delete=models.CASCADE)
    kkmCheck = models.FileField(upload_to='kkm/')
    referral = models.FileField(upload_to='napravleniya/', null=True, blank=True)
    invoice = models.FileField(upload_to='schet-fakturi/', null=True, blank=True)
    opinions_on_medications = models.FileField(upload_to='zaklucheniyaMedicamenty/', null=True, blank=True)
    sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dateTime = models.DateTimeField(null=True, blank=True)
    inn = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return self.dateTime
