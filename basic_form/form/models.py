from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=35)
    batch = models.IntegerField()
    course = models.CharField(max_length=25)

class Info(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=20)
    Re_Email = models.EmailField(max_length=20)
    Batch = models.IntegerField()
    password = models.CharField(max_length=40)
    re_password = models.CharField(max_length=40)
    textarea = models.CharField(max_length=50)
    checkbox = models.CharField(max_length=50)
    payments = models.DecimalField(max_digits=6,decimal_places=2)
    django = models.BooleanField()

