from rest_framework import generics, permissions

from tariffs.models import Tariff
from tariffs.serializers import TariffSerializer


class TariffListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TariffSerializer

    def get_queryset(self):
        return Tariff.objects.all()
