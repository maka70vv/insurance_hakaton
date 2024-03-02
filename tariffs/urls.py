from django.urls import path

from tariffs.views import TariffListView

urlpatterns = [
    path('tariffs/', TariffListView.as_view())
]