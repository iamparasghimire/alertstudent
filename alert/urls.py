from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chart/', views.chart, name='chart'),
    path('table/', views.table, name='table'),
    path('note/', views.note, name='note'),
    path('notesingle/', views.notesingle, name='notesingle'),
    path('notice/', views.notice, name='notice'),
    path('createtable/', views.createtable, name='createtable'),
    path('createnote/', views.createnote, name='createnote'),
    path('createnotice/', views.createnotice, name='createnotice'),


    path('register/', views.register, name='register'),
    path('password/', views.password, name='password'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),


]