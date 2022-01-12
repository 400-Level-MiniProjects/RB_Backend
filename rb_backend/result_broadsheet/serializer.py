from django.db.models import fields
from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    faculty = serializers.StringRelatedField()
    courses = serializers.StringRelatedField(many=True)
    class Meta:
        model = Department
        fields = '__all__'