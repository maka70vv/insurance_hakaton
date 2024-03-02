from rest_framework import serializers

from insurance_companies.models import Company
from policies.models import DMSPolicy
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        extra_kwarg = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        try:
            dms_policy = DMSPolicy.objects.get(inn=validated_data['inn'])
            dms_policy.user = user
            dms_policy.save()
        except DMSPolicy.DoesNotExist:
            pass
        try:
            insurance_company = Company.objects.get(inn=validated_data['inn'])
            user.company_instance = insurance_company
            user.is_insurance_company = True
            user.save()
        except Company.DoesNotExist:
            pass
        return user

    def update(self, instance, validated_data):
        instance.iin = validated_data.get("iin", instance.iin)
        instance.iban = validated_data.get("iban", instance.iban)
        instance.save()
