from django.urls import path
from .views import *
# from . import views

urlpatterns=[
    path('',insert,name='insert'),
    path('show/',show,name='show'),
    path('delete-post/<int:post_id>',delete_post,name='delete_post'),
    path('update-post/<int:post_id>',update_post,name='update_post'),
]