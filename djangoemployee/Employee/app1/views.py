from django.shortcuts import render
from app1.form import employeeForm
from app1.form import employee
# Create your views here.

def home(request):
    return render(request,'index.html',)

def table(request):
    k=employee.objects.all()
    return render(request,'table.html',{"x":k})

def form(request):
    form= employeeForm()
    if request.method=='POST':
        form=employeeForm(request.POST)
        if form.is_valid():
            form.save()
            return table(request)
        else:
            form=employeeForm()
    return render(request,'form.html',{"form":form})