from rest_framework import generics
from rest_framework.response import Response

from insurance_companies.models import Company
from insurance_companies.serializers import InsuranceCompanySerializer


class InsuranceCompaniesView(generics.ListAPIView):
    serializer_class = InsuranceCompanySerializer
    queryset = Company.objects.all()
    