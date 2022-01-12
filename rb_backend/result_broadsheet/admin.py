from django.contrib import admin
from .models import *

# Register AdminModels here

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name',)
    search_fields = ('department_name', 'courses')

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_name',)
    search_fields = ('faculty_name',)

# Register your models here.

admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Result)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Semester)