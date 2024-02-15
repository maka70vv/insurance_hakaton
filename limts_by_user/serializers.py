from rest_framework import serializers

from limts_by_user.models import LimitsByUser


class LimitByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LimitsByUser
        fields = '__all__'
