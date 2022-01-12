from django.http.response import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import *
from .serializer import DepartmentSerializer
from rest_framework import status


# Create your views here.
def index(request):
    return HttpResponse()

class CourseList(APIView):
    def get_object(self):
        try:
            return Department.objects.all()
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        data = self.get_object()
        serializer = DepartmentSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GenerateBroadsheet(APIView):
    def get(self, request, format=None):
        return Response("Generate Broadsheet")
    
class AddStudentResult(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            return Response('Deleted Your Result! HA! HA!! HA!!!')
        return Response("Add Student Result")
        pass