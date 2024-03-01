from django.urls import path

from policies import views

urlpatterns = [
    path('accidient/create/', views.AccidentPolicyCreateAPIViewWithCommission.as_view(), name='')
]