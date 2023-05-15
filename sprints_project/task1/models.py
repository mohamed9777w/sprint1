from django.db import models
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=500)

class Courses(models.Model):
    c_name = models.CharField(max_length=150)
    c_number = models.IntegerField()
    c_description = models.CharField(max_length=1000)
    c_duration = models.CharField(max_length=100)

