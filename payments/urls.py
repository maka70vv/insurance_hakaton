from django.urls import path

from payments.views import ReceiptUploadView

urlpatterns = [
    path('payment/request/', ReceiptUploadView.as_view(), name='payment-request')
]