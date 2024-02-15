from rest_framework import serializers

from limts_by_user.models import LimtsByUser


class LimitByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LimtsByUser
        fields = '__all__'
