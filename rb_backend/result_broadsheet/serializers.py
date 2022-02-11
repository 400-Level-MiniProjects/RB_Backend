from rest_framework import serializers
from . import models

# Write your serializers here
class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faculty
        fields = "__all__"

def serializeFaculty(facultyOBJ, many=False):
    if many is not False:
        serializer = FacultySerializer(facultyOBJ, many=True)
        return serializer.data
    else:
        serializer = FacultySerializer(facultyOBJ)
        return serializer.data

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = "__all__"

def serializeDepartment(departmentOBJ, many=False):
    if many is not False:
        serializer = DepartmentSerializer(departmentOBJ, many=True)
        return serializer.data
    else:
        serializer = DepartmentSerializer(departmentOBJ)
        return serializer.data


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"

def serializeCourse(courseOBJ, many=False):
    if many is not False:
        serializer = CourseSerializer(courseOBJ, many=True)
        return serializer.data
    else:
        serializer = CourseSerializer(courseOBJ)
        return serializer.data
class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Result
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = "__all__"

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lecturer
        fields = "__all__"

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Grade
        fields = "__all__"

