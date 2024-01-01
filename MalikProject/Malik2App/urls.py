from django.urls import path
from . import views

urlpatterns=[
    path(, views.index),
    path(NY, views.NewYear, name=NY),
    # path(<str:newyear>, views.fnc_name),
    path(tasks, views.tasks_funct, name=tasks),
    path(addtask, views.add_task, name=addtask)
]
