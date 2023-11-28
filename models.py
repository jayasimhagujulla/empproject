from django.db import models
from django.utils import timezone
# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=30)
    phoneno=models.IntegerField()
    address=models.CharField(max_length=30)
    hno=models.IntegerField()
    street=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
class WorkExperience(models.Model):
    companyname=models.CharField(max_length=30)
    fromdate=models.DateTimeField()
    todate=models.DateTimeField(default=timezone.now)
    address=models.CharField(max_length=30)
class Qualifications(models.Model):
    QualificationsName=models.CharField(max_length=30)
    fromdate=models.DateField()
    todate=models.DateField()
    percentage=models.IntegerField()
class projects(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=2000)
    