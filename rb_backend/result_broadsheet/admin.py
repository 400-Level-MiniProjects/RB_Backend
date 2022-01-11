from django.contrib import admin
from .models import *

# Register AdminModels here

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'date_joined',)
    search_fields = ('email', 'first_name', 'last_name',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('mat_no', 'level',)
    search_fields = ('mat_no',)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(CourseAdviser)
admin.site.register(Lecturer)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Result)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Semester)