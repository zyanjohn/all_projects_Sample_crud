from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fname(request):
    return HttpResponse('hello django')
def name(request):
    return HttpResponse('hello page2')