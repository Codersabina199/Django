from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login, logout
# Create your views here.
from .forms import UserCreationForm,UserLoginForm

def register(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'users/register.html',{'form':form})

def Userlogin(request):
    form=UserLoginForm()
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form .is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponse("Logged in succeesfully")
            else:
                return HttpResponse("Invalid credentials")
    return render(request,'users/login.html',{'form':form})
            
        
def logout_user(request):
    logout(request)
    return HttpResponse("Logged out successfully")
