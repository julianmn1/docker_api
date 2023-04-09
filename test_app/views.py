from rest_framework.views import APIView
from django.http import JsonResponse

# Create your views here.
class TestView(APIView):

    def get(self, request):
        return JsonResponse({"message": "Hello there!"})