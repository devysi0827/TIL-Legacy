from django.db import models


# Create your models here.
class Student(models.Model):
    pass
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    major = models.CharField(max_length=100)
    hobby = models.TextField()

Student # => table

