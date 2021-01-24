from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path('', views.note, name='note'),
    path('faculty/', views.faculty, name='faculty'),
    path('notesingle/', views.notesingle, name='notesingle'),

    path('createnote/', views.createnote, name='createnote'),
  




]