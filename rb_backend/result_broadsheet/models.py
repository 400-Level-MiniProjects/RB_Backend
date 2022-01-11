from django.db import models
# This is used for translation
from django.utils.translation import deactivate, gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


# Create your models here.

class Faculty(models.Model):
    faculty_name =models.CharField(max_length=200, blank=False)

    def __str__(self) -> str:
        return self.faculty_name

class Department(models.Model):
    department_name = models.CharField(max_length=150, blank=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.department_name
# User-Based Models

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Please, enter a Valid email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('set staff to be true'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('set superuser to be true'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email_address'), unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    date_joined = models.DateTimeField((_('date_joined')), auto_now_add=True)
    is_active = models.BooleanField((_('is_active')), default=True)
    is_staff = models.BooleanField((_('is_staff')), default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'User'

# Can you please add department as part of the fields
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mat_no = models.CharField(max_length=20, blank=False)
    level = models.CharField(max_length=6, blank=False)
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Student'


class CourseAdviser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'CourseAdviser'


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


class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Lecturer'

class Course(models.Model):
    course_name = models.CharField(max_length=200, blank=False)
    course_code = models.CharField(max_length=50, blank=False)
    credit_unit = models.IntegerField(blank=False)
    c_a_score = models.DecimalField(max_digits=3, decimal_places=2, blank=True, default=0)
    exam_score = models.DecimalField(max_digits=3, decimal_places=2, blank=True, default=0)

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
