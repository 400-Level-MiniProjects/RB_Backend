from django.http.response import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse()

class CourseList(APIView):
    def get(self, request):
        return Response('GREAT!')

class GenerateBroadsheet(APIView):
    def get(self, request, format=None):
        return Response("Generate Broadsheet")
    
class AddStudentResult(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            return Response('Deleted Your Result! HA! HA!! HA!!!')
        return Response("Add Student Result")
        pass