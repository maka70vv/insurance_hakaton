from rest_framework import serializers

from policies.models import AccidentPolicy, CarPolicy, CargoPolicy, VZRPolicy, DMSPolicy


class AccidentPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccidentPolicy
        fields = '__all__'


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
