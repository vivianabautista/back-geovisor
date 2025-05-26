from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Form
from .serializers import FormSerializer

class FormSearchView(APIView):
    def get(self, request, search=None):
        if search:
            forms = Form.objects.filter(name__icontains=search)
        else:
            forms = Form.objects.all()
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)