from django.contrib.staticfiles.storage import staticfiles_storage
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics, permissions

from cars_damages_process.models import DamagePaymentsRange
from limts_by_user.models import LimitsByUser
from payments.ai_interation import AiInteration
from payments.models import MedicalPaymentRequest, VZRPaymentRequest, GruzPaymentRequest, CarPaymentRequest
from payments.serializers import PaymentSerializer, VZRPaymentSerializer, GruzPaymentSerializer, CarPaymentSerializer
from payments.services import ProcessQR


class ReceiptUploadView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MedicalPaymentRequest.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        qr = serializer.validated_data.get("kkmCheck")
        print(qr)
        # processQR = ProcessQR()
        # inn, dateTime, summ, is_medical = processQR.process_receipt_image(qr)
        inn, dateTime, summ, is_medical = "02111293219032", "2024-05-16", 200, True
        user = self.request.user
        service = serializer.validated_data.get("service")
        policy = serializer.validated_data.get("policy")
        print(policy)
        limitName = service.verboseLimitName

        if is_medical:
            limitsByUser = LimitsByUser.objects.get(user=user, limitName=limitName, policy_num=policy.policy_num)
            if limitsByUser.summ >= summ:
                finalSumm = summ
                limitsByUser.summ -= summ
                limitsByUser.save()
            else:
                finalSumm = limitsByUser.summ

            payment_request = MedicalPaymentRequest(
                user=user,
                kkmCheck=qr,
                sum=summ,
                dateTime=dateTime,
                inn=inn,
                limit=LimitsByUser.objects.get(user=user, limitName=limitName),
                service=service
            )

            payment_request.save()

            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response("Not medical service!", status=status.HTTP_400_BAD_REQUEST)


class MedicalPaymentByUserView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PaymentSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = MedicalPaymentRequest.objects.filter(user=user)
        return queryset


class VZRPaymentView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = VZRPaymentSerializer

    def post(self, request, **kwargs):
        user = self.request.user
        summ = request.data.get("summ")
        service = request.data.get("service")
        # limitName = service.verboseLimitName
        # limitsByUser = LimitsByUser.objects.get(user=user, limitName=limitName)
        # if limitsByUser.summ < summ:
        #     summ = limitsByUser.summ
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['summ'] = summ
        serializer.save()
        return Response("OK", status=status.HTTP_200_OK)


class VZRPaymentProcess(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = VZRPaymentRequest.objects.all()
    serializer_class = VZRPaymentSerializer

    def update(self, request, *args, **kwargs):
        if self.request.user.is_insurance_company:
            instance = self.get_object()
            approved = request.data.get('approved')
            final_summ = request.data.get('final_summ')
            service = request.data.get("service")
            limitName = service.verboseLimitName

            if approved:
                instance.approved = True
                # limitsByUser = LimitsByUser.objects.get(user=instance.user, limitName=limitName)
                # limitsByUser.summ -= final_summ
                instance.processed = True
                serializer = self.get_serializer(instance, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                return Response(serializer.data)
            else:
                instance.approved = False
                instance.processed = True
                serializer = self.get_serializer(instance, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class VZRPaymentByUserView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = VZRPaymentSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = VZRPaymentRequest.objects.filter(user=user)
        return queryset


class CargoPaymentRequestCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GruzPaymentSerializer
    queryset = GruzPaymentRequest.objects.all()

    def post(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = self.request.user
        serializer.save()
        return Response("OK", status=status.HTTP_200_OK)


class CargoPaymentRequestUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GruzPaymentSerializer
    queryset = GruzPaymentRequest.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        approved = request.data.get('approved')

        if approved:
            instance.approved = True
            instance.processed = True
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance.approved = False
            instance.processed = True
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)


class CargoPaymentRequestDetailView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GruzPaymentSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = GruzPaymentRequest.objects.filter(user=user)
        return queryset


class CarPaymentRequestCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CarPaymentSerializer
    queryset = CarPaymentRequest.objects.all()

    def perform_create(self, serializer):
        user = self.request.user

        serializer.validated_data['user'] = self.request.user

        serializer = self.serializer_class(data=serializer.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        ai = AiInteration()
        image_obj = serializer.instance.image

        # # Получаем URL-адрес изображения
        # if image_obj:
        #     image_url = staticfiles_storage.url(
        #         image_obj.name)  # Получаем URL-адрес изображения из статических файлов Django
        # else:
        #     image_url = None
        #
        # if image_url:
        damage_degree = ai.ai_integration(image_obj) * 100
        try:
            recommended_summ = DamagePaymentsRange.objects.get(min_damage__lte=damage_degree,
                                                               max_damage__gte=damage_degree).payment_summ
        except DamagePaymentsRange.DoesNotExist:
            recommended_summ = None
            return Response("Соответствующий диапазон для урона не найден", status=status.HTTP_400_BAD_REQUEST)

        serializer.data['recommended_summ'] = recommended_summ

        return Response("OK", status=status.HTTP_200_OK)
    # else:
    #     return Response("URL изображения не найден", status=status.HTTP_400_BAD_REQUEST)
    #


class CarPaymentRequestUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CarPaymentSerializer
    queryset = CarPaymentRequest.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        approved = request.data.get('approved')

        if approved:
            instance.approved = True
            instance.processed = True
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance.approved = False
            instance.processed = True
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)


class CarPaymentRequestByUserView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CarPaymentSerializer

    def get_queryset(self):
        queryset = CarPaymentRequest.objects.filter(user=self.request.user)
        return queryset


class DMSPaymentsForInsuranceCompanies(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MedicalPaymentRequest.objects.all()
    serializer_class = PaymentSerializer

    def get_queryset(self):
        company = self.request.user.company_instance
        queryset = MedicalPaymentRequest.objects.filter(insurance_company=company)
        return queryset


class VZRPaymentsForInsuranceCompanies(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = VZRPaymentRequest.objects.all()
    serializer_class = VZRPaymentSerializer

    def get_queryset(self):
        company = self.request.user.company_instance
        queryset = VZRPaymentRequest.objects.filter(insurance_company=company)
        return queryset


class CargoPaymentsForInsuranceCompanies(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = GruzPaymentRequest.objects.all()
    serializer_class = GruzPaymentSerializer

    def get_queryset(self):
        company = self.request.user.company_instance
        queryset = GruzPaymentRequest.objects.filter(insurance_company=company)
        return queryset


class CarPaymentsForInsuranceCompanies(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CarPaymentRequest.objects.all()
    serializer_class = CarPaymentSerializer

    def get_queryset(self):
        company = self.request.user.company_instance
        queryset = CarPaymentRequest.objects.filter(insurance_company=company)
        return queryset
