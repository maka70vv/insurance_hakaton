from rest_framework import serializers

from insurance_companies.models import Company


class InsuranceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
