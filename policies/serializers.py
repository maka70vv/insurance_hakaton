from rest_framework import serializers

from policies.models import AccidentPolicy, CarPolicy, CargoPolicy, VZRPolicy, DMSPolicy


class AccidentPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccidentPolicy
        fields = '__all__'

    def save(self, **kwargs):
        user = self.context['request'].user
        summ = self.context['request'].data.get("summ")
        insurance_company = self.context['request'].data.get("insurance_company")
        commission_by_company = insurance_company.commission
        commission_summ = int(summ) * int(commission_by_company) / 100
        price_with_commission = int(summ) + commission_summ

        validated_data = {**self.validated_data, 'user': user,
                          'commission_summ': commission_summ,
                          'price_with_commission': price_with_commission}

        accident_policy = AccidentPolicy.objects.create(**validated_data)
        return accident_policy


class CarPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPolicy
        fields = '__all__'


class CargoPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoPolicy
        fields = '__all__'


class VZRPolicySerializer(serializers.Serializer):
    class Meta:
        model = VZRPolicy
        fields = '__all__'


class DMSPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = DMSPolicy
        fields = '__all__'
