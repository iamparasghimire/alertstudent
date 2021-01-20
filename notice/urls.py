from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
 
    path('notice/', views.notice, name='notice'),

    path('createnotice/', views.createnotice, name='createnotice'),


  


]