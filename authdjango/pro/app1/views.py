from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from app1.forms import userForm
def home(request):
    return render(request,'home.html')

# def signUp1(request):
#     form = userForm()
#     if(request.method=='POST'):
#         form = userForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return home(request)

#     return render(request,'signup1.html',{"form": form})



def base(request):
    return render(request,'base.html')



#######################################################################
def home(request):

    return render(request, 'home.html')
def base(request):
    return render(request,'base.html')


def signUp1(request):
   form = UserCreationForm()
   if(request.method=='POST'):
       form = UserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           return home(request)

   return render(request, 'signup1.html', {"form": form})
########################################################################
def user_login1(request):
    if(request.method=="POST"):
        name = request.POST['n']
        password = request.POST['p']
        user = authenticate(username=name, password=password)
        if user:
            login(request,user)
            
            return home(request)
      
        else:
             return HttpResponse('invalid ...no user found')
    return render(request, 'login1.html')

def user_logout1(request):
        logout(request)
        return user_login1(request)
######