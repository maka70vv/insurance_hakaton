from rest_framework import serializers

from payments.models import MedicalPaymentRequest, VZRPaymentRequest


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalPaymentRequest
        fields = '__all__'


class VZRPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VZRPaymentRequest
        fields = '__all__'
