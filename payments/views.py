from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pyzbar.pyzbar import decode
from PIL import Image


class ReceiptUploadView(APIView):
    def post(self, request, format=None):
