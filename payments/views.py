from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from limts_by_user.models import LimitsByUser
from payments.models import MedicalPaymentRequest
from payments.serializers import PaymentSerializer
from payments.services import ProcessQR


class ReceiptUploadView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MedicalPaymentRequest.objects.all()
    serializer_class = PaymentSerializer
    def perform_create(self, serializer):
        qr = serializer.validated_data.get("kkmCheck")
        processQR = ProcessQR()
        inn, dateTime, summ = processQR.process_receipt_image(qr)
        user = serializer.validated_data["user"]
        service = serializer.validated_data.get("service")
        limitName = service.verboseLimitName

        payment_request = MedicalPaymentRequest(
            user=user,
            kkmCheck=qr,
            sum=summ,
            dateTime=dateTime,
            inn=inn,
            limit=LimitsByUser.objects.filter(user=user, limitName=limitName),
            service=service
        )

        payment_request.save()

        return Response(status=status.HTTP_201_CREATED)


