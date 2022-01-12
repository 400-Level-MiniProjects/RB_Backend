from django.db import models
from django.utils.translation import deactivate, gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

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

class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Lecturer'
