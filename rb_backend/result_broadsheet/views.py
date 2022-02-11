from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializers import *

from .models import *
from .serializers import *
# Create your views here.
class FacultyData(APIView):
    def get(self, request, pk=None):
        faculty_data = {}

        if pk is not None:
            """[This gets the faculty detail if 'pk' is present in the request]

            Returns:
                [API Response]: [The response carries the single Faculty response to the view]
            """
            facultyOBJ = Faculty.objects.get(pk=pk)
            faculty_ = serializeFaculty(facultyOBJ)
            faculty_data['data'] = "Faculty Detail"
            faculty_data['details'] = faculty_
            return Response(faculty_data)

        """[If the 'pk' paramerter doesn't exist]

        Returns:
            [API Response]: [The response carries all the Faculty responses to the view]
        """
        facultyOBJ = Faculty.objects.all()
        faculties = serializeFaculty(facultyOBJ, many=True)
        faculty_data['data'] = "Faculty List"
        faculty_data['details'] = faculties
        return Response(faculty_data)

    def post(self, request, pk=None):
        if pk is not None:
            facultyOBJ = Faculty.objects.get(pk=pk)
            serializer = FacultySerializer(facultyOBJ, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"Error": "invalid request!!!"})
        else:
            # faucltyOBJ = Faculty.objects.
            serializer = FacultySerializer(data=request.data)
            if serializer.is_valid():
                try :
                    facultyOBJ = Faculty.objects.get(faculty_code = request.data['faculty_code'])
                    if facultyOBJ:
                        return Response({"Error": "Data Exists!"})
                except Faculty.DoesNotExist:
                    serializer.save()
                    return Response(serializer.data)
            else:
                return Response({"Error": "invalid request!!!"})

    def delete(self, request, pk=None):
        if pk is not None:
            facultyOBJ = Faculty.objects.get(pk=pk)
            serializer = FacultySerializer(facultyOBJ, data=request.data)

            if serializer.is_valid():
                serializer.delete()
                return Response(serializer.data)
            else:
                return Response({"Error": "invalid request!!!"})

        else:
                return Response({"Error": "invalid request!!!"})

class DepartmentData(APIView):
    def get(self, request, d_code=None):
        if d_code is not None:
            """[if the department code (d_code is given in the request)]

            Returns:
                Response: [returns the detail of the department]
            """
        
            d_code = str(d_code.upper())
            deptOBJ = Department.objects.get(department_code=d_code)
            department_ = serializeDepartment(deptOBJ)

            return Response(department_)
        else:
            depts_dict={
                "data":"List of Departments by Faculty",
                "dept_data":list()
            }

            dept_data = list()
            deptOBJ = Department.objects.all()
            departments = serializeDepartment(deptOBJ, many=True)

            facultyOBJ = Faculty.objects.all()
            faculties = serializeFaculty(facultyOBJ, many=True)

            for faculty in faculties:
                dept={}
                dept['faculty']=faculty['faculty_name']
                dept['faculty_code']=faculty['faculty_code']
                dept['departments']=list()

                for department in departments:
                    if department['faculty']== faculty['id']:
                        dept['departments'].append(str(department['department_name']+" ("+department['department_code']+")"))
                dept_data.append(dept)

            depts_dict['dept_data']=dept_data
            return Response(depts_dict)

    def post(self, request, pk=None):
        pass

    def delete(self, request, pk=None):
        pass

class CourseData(APIView):
    def get(self, request, pk=None):
        courseOBJ = Course.objects.all()
        courses = serializeCourse(courseOBJ, many=True)
        return Response(courses)

    def post(self, request, pk=None):
        pass

