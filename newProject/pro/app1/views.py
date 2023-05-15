from django.shortcuts import render
from django.contrib.auth import forms
from app1.form import bookForm
from app1.models import books
# Create your views here.


def base(request):
    return render(request,'base.html')

def upload(request):
    if (request.method=="POST"):
        title=request.POST['title']
        author=request.POST['author']
        pdf=request.POST['pdfs']
        cover=request.POST['cover']
        store=books.objects.create(title=title,author=author,pdf=pdf,cover=cover)
        store.save()
        return base(request)
    return render(request,'upload.html')


def showbooks(request):
    k=books.objects.all()
    return render(request,'showbooks.html',{"s":k})


def delete_book(request,p):
    s=books.objects.get(pk=p)
    s.delete()
    return showbooks(request)
     

def edit_book(request,p):
    d=books.objects.get(pk=p)
    form=bookForm(instance=d)
    if (request.method=='POST'):
         form=bookForm(request.POST,instance=d)
         if(form.is_valid()):
              form.save()
              return showbooks(request)
    return render(request,'upload.html',{'form':form})