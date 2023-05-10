from django.db import models

# Create your models here.

class employee(models.Model):
    employee_name=models.CharField(max_length=20)
    employee_age=models.IntegerField()
    emp_id=models.IntegerField()
    employee_salary=models.IntegerField()