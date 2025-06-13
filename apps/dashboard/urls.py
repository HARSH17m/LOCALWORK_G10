from django.urls import path
from .views import *
# from . import views

urlpatterns=[
    path('',insert,name='insert'),
    path('show/',show,name='show'),
]