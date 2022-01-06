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