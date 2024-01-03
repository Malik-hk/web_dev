from django.shortcuts import render, HttpResponse

# Create your views here.

def index(req):
    return render(req, '/home/malik/test_website/Athentication page/web_app/templates/web_app/index.html')

def login(req):
    return render(req, '/home/malik/test_website/Athentication page/web_app/templates/web_app/login.html')

def logout(req):
    return HttpResponse('Logout page')

def register(req):
    return render(req, '/home/malik/test_website/Athentication page/web_app/templates/web_app/register.html')

