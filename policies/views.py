from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from insurance_companies.models import Company
from policies.models import AccidentPolicy
from policies.serializers import AccidentPolicySerializer


class AccidentPolicyAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AccidentPolicySerializer

    def get_queryset(self):
        user = self.request.user
        return AccidentPolicy.objects.filter(user=user)


class AccidentPolicyCreateAPIViewWithCommission(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AccidentPolicySerializer
    queryset = AccidentPolicy.objects.all()

    def post(self, request, *args, **kwargs):
        user = request.user.id
        summ = request.data.get("price")
        company_id = request.data.pop("insurance_company")
        insurance_company = Company.objects.get(id=company_id)
        commission_by_company = insurance_company.commission
        commission_summ = int(summ) * int(commission_by_company) / 100
        price_with_commission = int(summ) + commission_summ

        accident_policy = AccidentPolicy(
            user_id=user,
            commission_summ=commission_summ,
            price_with_commission=price_with_commission,
            insurance_company=insurance_company,
            **request.data
        )

        accident_policy.save()

        accident_policy.policy_num = f"НС№{accident_policy.id}"
        accident_policy.save()

        serializer = self.get_serializer(accident_policy)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
