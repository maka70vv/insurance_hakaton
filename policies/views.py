from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from insurance_companies.models import Company
from policies.exel_process import parse
from policies.models import AccidentPolicy, CarPolicy, CargoPolicy, VZRPolicy, DMSPolicy
from policies.serializers import AccidentPolicySerializer, CarPolicySerializer, CargoPolicySerializer, \
    VZRPolicySerializer, DMSPolicySerializer
from tariffs.models import Tariff
from users.models import User


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


class CarPolicyCreateAPIViewWithCommission(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CarPolicySerializer
    queryset = CarPolicy.objects.all()

    def post(self, request, *args, **kwargs):
        user = request.user.id
        summ = request.data.get("price")
        company_id = request.data.pop("insurance_company")
        insurance_company = Company.objects.get(id=company_id)
        commission_by_company = insurance_company.commission
        commission_summ = int(summ) * int(commission_by_company) / 100
        price_with_commission = int(summ) + commission_summ

        car_insurance = CarPolicy(
            user_id=user,
            commission_summ=commission_summ,
            price_with_commission=price_with_commission,
            insurance_company=insurance_company,
            **request.data
        )

        car_insurance.save()

        car_insurance.policy_num = f"КАСКО№{car_insurance.id}"
        car_insurance.save()

        serializer = self.get_serializer(car_insurance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CargoPolicyCreateAPIViewWithCommission(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CargoPolicySerializer
    queryset = CargoPolicy.objects.all()

    def post(self, request, *args, **kwargs):
        user = request.user.id
        summ = request.data.get("price")
        company_id = request.data.pop("insurance_company")
        insurance_company = Company.objects.get(id=company_id)
        commission_by_company = insurance_company.commission
        commission_summ = int(summ) * int(commission_by_company) / 100
        price_with_commission = int(summ) + commission_summ

        car_insurance = CargoPolicy(
            user_id=user,
            commission_summ=commission_summ,
            price_with_commission=price_with_commission,
            insurance_company=insurance_company,
            **request.data
        )

        car_insurance.save()

        car_insurance.policy_num = f"ГРУЗ№{car_insurance.id}"
        car_insurance.save()

        serializer = self.get_serializer(car_insurance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VZRPolicyCreateAPIViewWithCommission(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VZRPolicySerializer
    queryset = VZRPolicy.objects.all()

    def post(self, request, *args, **kwargs):
        user = request.user.id
        summ = request.data.get("price")
        company_id = request.data.pop("insurance_company")
        insurance_company = Company.objects.get(id=company_id)
        commission_by_company = insurance_company.commission
        commission_summ = int(summ) * int(commission_by_company) / 100
        price_with_commission = int(summ) + commission_summ

        vzr_insurance = VZRPolicy(
            user_id=user,
            commission_summ=commission_summ,
            price_with_commission=price_with_commission,
            insurance_company=insurance_company,
            **request.data
        )

        vzr_insurance.save()

        vzr_insurance.policy_num = f"ВЗР№{vzr_insurance.id}"
        vzr_insurance.save()

        serializer = self.get_serializer(vzr_insurance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class DMSPolicyCreateAPIViewWithCommission(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = DMSPolicySerializer
#     queryset = DMSPolicy.objects.all()
#
#     def post(self, request, *args, **kwargs):
#         exel_form = request.data.get("exel_form")
#         workers = parse(exel_form)
#
#         for worker in workers.values():
#             inn = worker[0]
#             fam1_inn = worker[1]
#             fam2_inn = worker[2]
#             summ = request.data.get("price")
#             company_id = request.data.get("insurance_company")
#             tariff_id = request.data.get("tariff")
#             try:
#                 tariff = Tariff.objects.get(id=tariff_id)
#             except Tariff.DoesNotExist:
#                 return Response(tariff_id)
#             insurance_company = Company.objects.get(id=company_id)
#             commission_by_company = insurance_company.commission
#             commission_summ = int(summ) * int(commission_by_company) / 100
#             price_with_commission = int(summ) + commission_summ
#
#             request_data = request.data.copy()
#             request_data.pop("exel_form")
#             request_data.pop("tariff")
#
#             dms_insurance = DMSPolicy(
#                 inn=inn,
#                 fam_member1_inn=fam1_inn,
#                 fam_member2_inn=fam2_inn,
#                 commission_summ=commission_summ,
#                 price_with_commission=price_with_commission,
#                 tariff=tariff,
#                 # insurance_company=insurance_company,
#                 **request.data
#
#                 )
#
#             dms_insurance.save()
#
#         return Response({"message": "Data created successfully"}, status=status.HTTP_201_CREATED)
#
