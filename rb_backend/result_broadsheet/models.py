from django.db import models
from accounts.models import *

# Create your models here.

class Session(models.Model):
    pass

class Semester(models.Model):
    SEMESTER=(
        ('F','First Semester' ),
        ('S', 'Second Semester')
    )
    semester_name = models.CharField(max_length=1, choices=SEMESTER, blank=False)

    def __str__(self) -> str:
        return self.semester_name
    
    class Meta:
        verbose_name_plural = "Semester"

class Course(models.Model):
    course_name = models.CharField(max_length=200, blank=False)
    course_code = models.CharField(max_length=50, blank=False)
    credit_unit = models.IntegerField(blank=False)
    c_a_score = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    exam_score = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)

    def __str__(self) -> str:
        return "("+self.course_code+") "+self.course_name

    class Meta:
        verbose_name_plural = "Course"


class Grade(models.Model):
    grade_code = models.CharField(max_length=1, blank=False)
    grade_point = models.DecimalField(max_digits=3, decimal_places=3, blank=False)
    
    def __str__(self) -> str:
        return self.grade_code+" ("+self.grade_point+")"
    


class Result(models.Model):
    SEMESTER=(
        ('F','First Semester' ),
        ('S', 'Second Semester')
    )
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,  on_delete=models.CASCADE)
    c_a_score = models.DecimalField(max_digits=3, decimal_places=2, blank=True, default=0)
    exam_score = models.DecimalField(max_digits=3, decimal_places=2, blank=True, default=0)
    grade = models.ForeignKey(Grade, default=6, on_delete=models.CASCADE)
    # session = models.TextChoices('Session', 'FIRST SECOND')
    semester = models.CharField(max_length=1, choices=SEMESTER, blank=False)
    
    def __str__(self) -> str:
        return self.student+" ("+self.grade+")"

    class Meta:
        verbose_name_plural = 'Result'


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=50, blank=False)
    faculty_code = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.faculty_name

    class Meta:
        verbose_name_plural = 'Faculty'

class Department(models.Model):
    department_name = models.CharField(max_length=150, blank=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, default=None)

    def __str__(self) -> str:
        return self.department_name
    
    class Meta:
        verbose_name_plural = 'Department'

# class CA_Result():
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course,  on_delete=models.CASCADE)
#     c_a_score = models.IntegerField(blank=True, default=0)
    
#     def __str__(self) -> str:
#         return self.student+" ("+self.course+" "+self.c_a_score+")"


# class SemesterResult():
#     pass


# class SessionResult():
#     pass
