from django.urls import path
#now import the views.py file into this code
from . import views

urlpatterns = [    
    path(,views.index),
    path(newyear, views.NEWYEAR),
    # path(<str:name>, views.anybody)
    path(html5, views.MyHtml)

]
