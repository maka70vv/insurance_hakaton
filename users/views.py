from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import UserSerializer


# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
