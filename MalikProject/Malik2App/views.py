from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def index(request):
    return render(request, Malik2App/index.html)
    return HttpResponse(Hello! This is Malik2App index page.)
    
def NewYear(request):
    return HttpResponse(This is another new year from Malik2App)

def fnc_name(request, newyear):
    today = datetime.datetime.now()    #       -->               It will get todays date.
    return render(request, Malik2App/newyear.html, {
        newyear: today.month == 11 and today.day == 12   #     if today date & month is 1
    })

Tasks = [foo, bar, baz]
def tasks_funct(request):
    return render(request, Malik2App/tasks.html, {
        tasks: Tasks
    })

def add_task(request):
    return render(request, Malik2App/add_tasks.html)

