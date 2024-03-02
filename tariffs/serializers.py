from rest_framework import serializers

from tariffs.models import Tariff


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'
