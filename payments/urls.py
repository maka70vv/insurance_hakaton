from django.urls import path

from payments.views import ReceiptUploadView, MedicalPaymentByUserView, VZRPaymentView, VZRPaymentProcess, \
    VZRPaymentByUserView, CargoPaymentRequestCreateView, CargoPaymentRequestDetailView, CargoPaymentRequestUpdateView, \
    CarPaymentRequestCreateView, CarPaymentRequestUpdateView, CarPaymentRequestByUserView, \
    DMSPaymentsForInsuranceCompanies, VZRPaymentsForInsuranceCompanies, CargoPaymentsForInsuranceCompanies, \
    CarPaymentsForInsuranceCompanies

urlpatterns = [
    path('payment/medical/request/', ReceiptUploadView.as_view(), name='medical-payment-request'),
    path('payment/medical/by_user/', MedicalPaymentByUserView.as_view(), name='payment_by_user'),
    path('payment/vzr/request/', VZRPaymentView.as_view(), name='vzr_payment_request'),
    path('payment/vzr/process/', VZRPaymentProcess.as_view(), name='vzr_payment_process'),
    path('payment/vzr/by_user/', VZRPaymentByUserView.as_view(), name='payment_by_user'),
    path('payment/cargo/request/', CargoPaymentRequestCreateView.as_view(), name="cargo_payment_request_create"),
    path('payment/cargo/by_user/', CargoPaymentRequestDetailView.as_view(), name=""),
    path('payment/cargo/process/', CargoPaymentRequestUpdateView.as_view(), name=""),
    path('payment/car/create/', CarPaymentRequestCreateView.as_view(), name=""),
    path('payment/car/process/', CarPaymentRequestUpdateView.as_view(), name=""),
    path('payment/car/by_user/', CarPaymentRequestByUserView.as_view()),
    path('payment/medical/insurance_company/', DMSPaymentsForInsuranceCompanies.as_view()),
    path('payment/vzr/insurance_company/', VZRPaymentsForInsuranceCompanies.as_view(), name=""),
    path('payment/cargo/insurance_company/', CargoPaymentsForInsuranceCompanies.as_view(), name=""),
    path('payment/cars/insurance_company/', CarPaymentsForInsuranceCompanies.as_view(), name="")
]
