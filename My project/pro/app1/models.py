from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    
# class employee(models.Model):
#     eid = models.IntegerField()
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()
#     place = models.CharField(max_length=30)
#     salary = models.IntegerField()
#     des = models.CharField(max_length=20)
