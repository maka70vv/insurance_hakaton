from django.urls import path

from insurance_companies.views import InsuranceCompaniesView

urlpatterns = [
    path('get_companies/', InsuranceCompaniesView.as_view())
]