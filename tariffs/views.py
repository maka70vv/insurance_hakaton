from rest_framework import generics

from tariffs.models import Tariff
from tariffs.serializers import TariffSerializer


class TariffListView(generics.ListAPIView):
    serializer_class = TariffSerializer

    def get_queryset(self):
        return Tariff.objects.all()
