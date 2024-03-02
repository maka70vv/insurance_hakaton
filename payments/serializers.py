from rest_framework import serializers

from payments.models import MedicalPaymentRequest, VZRPaymentRequest, GruzPaymentRequest, CarPaymentRequest


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalPaymentRequest
        fields = '__all__'


class VZRPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VZRPaymentRequest
        fields = '__all__'


class GruzPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GruzPaymentRequest
        fields = '__all__'


class CarPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPaymentRequest
        fields = '__all__'
