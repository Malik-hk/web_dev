from django.shortcuts import render, HttpResponse, redirect
import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(req):
    return render(req, 'web_app/index.html')

def login_view(req):
    if req.method=='POST':
        Email=req.POST.get('username')
        Pass=req.POST.get('psw')

        user = authenticate(req, username=Email, password=Pass)
        
        if user is not None:
            login(req, user)
            return HttpResponse("Login successful!")
        else:
            return HttpResponse("Sorry! try again")

    return render(req, 'web_app/login.html')

def logout_view(req):
    return HttpResponse('Logout page')

def register(req):
    if req.method=='POST':
        Email=req.POST.get('username')
        Pass=req.POST.get('psw')
        Pass1=req.POST.get('psw-repeat')

        user=User.objects.create_user(Email, Pass, Pass1)
        user.save()
        return HttpResponse("user has been created successfully")
        return redirect('login')









    return render(req, 'web_app/register.html')

