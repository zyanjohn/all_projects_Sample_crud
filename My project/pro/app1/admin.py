from django.contrib import admin

# Register your models here.
from app1.models import student
from app1.models import employee
admin.site.register(student)
admin.site.register(employee)
