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
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)

    class Meta:
        model = CarPaymentRequest
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.get('image')
        instance = super().create(validated_data)

        if image:
            instance.image = image
            instance.save()
        return instance
