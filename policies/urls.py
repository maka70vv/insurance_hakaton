from django.urls import path

from policies import views

urlpatterns = [
    path('accidient/create/platform/', views.AccidentPolicyCreateAPIViewWithCommission.as_view(), name=''),
    path('cars/create/platform/', views.CarPolicyCreateAPIViewWithCommission.as_view(), name=''),
    path('cargos/create/platform/', views.CargoPolicyCreateAPIViewWithCommission.as_view(), name=''),
    path('vzr/create/platform/', views.VZRPolicyCreateAPIViewWithCommission.as_view(), name=''),
    path('dms/create/', views.DMSPolicyCreateAPIViewWithCommission.as_view(), name='')
]
