from rest_framework import serializers

from payments.models import MedicalPaymentRequest


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalPaymentRequest
        fields = '__all__'