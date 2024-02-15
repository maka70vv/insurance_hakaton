from rest_framework import generics, permissions

from limts_by_user.models import LimitsByUser
from limts_by_user.serializers import LimitByUserSerializer


class UserLimitsListView(generics.ListAPIView):
    queryset = LimitsByUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LimitByUserSerializer
