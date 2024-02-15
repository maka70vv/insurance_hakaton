from rest_framework import generics, permissions

from limts_by_user.models import LimtsByUser
from limts_by_user.serializers import LimitByUserSerializer


class UserLimitsListView(generics.ListAPIView):
    queryset = LimtsByUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LimitByUserSerializer
