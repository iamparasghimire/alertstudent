from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path('', views.table, name='table'),

    path('createtable/', views.createtable, name='createtable'),


]
