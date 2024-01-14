from django.db import models


# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

