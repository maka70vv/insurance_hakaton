# serializers.py
from rest_framework import serializers
from .models import Analytica

class AnalyticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytica
        fields = '__all__'
