from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from policies.models import AccidentPolicy
from policies.serializers import AccidentPolicySerializer


class AccidentPolicyAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AccidentPolicySerializer

    def get_queryset(self):
        user = self.request.user
        return AccidentPolicy.objects.filter(user=user)


class AccidentPolicyCreateAPIViewWithCommission(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AccidentPolicySerializer
    queryset = AccidentPolicy.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = AccidentPolicySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
