# views.py
from rest_framework.generics import ListAPIView
from .models import Analytica
from .serializers import AnalyticaSerializer

class AnalyticaListView(ListAPIView):
    queryset = Analytica.objects.all()
    serializer_class = AnalyticaSerializer
