from django.urls import path

from payments.views import ReceiptUploadView, MedicalPaymentByUserView, VZRPaymentView, VZRPaymentProcess, \
    VZRPaymentByUserView

urlpatterns = [
    path('payment/medical/request/', ReceiptUploadView.as_view(), name='medical-payment-request'),
    path('payment/medical/by_user/', MedicalPaymentByUserView.as_view(), name='payment_by_user'),
    path('payment/vzr/request/', VZRPaymentView.as_view(), name='vzr_payment_request'),
    path('payment/vzr/process/', VZRPaymentProcess.as_view(), name='vzr_payment_process'),
    path('payment/vzr/by_user/', VZRPaymentByUserView.as_view(), name='payment_by_user')
]
