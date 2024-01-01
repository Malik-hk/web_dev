from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, MalikApp/index.html)

def NEWYEAR(request):
    return HttpResponse(This is New Year Eve)

def anybody(request, name):
    return HttpResponse(fHey {name}!)

def MyHtml(request):
    return render(request, MalikApp/index.html)

