#Imports
from django.http.response import HttpResponse
from django.urls import path
from . import views


# Urls here
urlpatterns =[
    path('courses/', views.CourseData.as_view(), name='Courses'),
    path('faculty/', views.FacultyData.as_view(), name='Faculties'),
    path('faculty/<str:f_code>/', views.FacultyData.as_view(), name='Faculty Detail'),
    path('dept/', views.DepartmentData.as_view(), name='Departments'),
    path('dept/<str:d_code>/', views.DepartmentData.as_view(), name='Department Detail'),
    path("result/", views.ResultData.as_view()),
    # path('generate-broadsheet/', views.GenerateBroadsheet.as_view()),
    # path('add-result/', views.AddStudentResult.as_view()),
    # path('del-result/<int:pk>', views.AddStudentResult.as_view())
]