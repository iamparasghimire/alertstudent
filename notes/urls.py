from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path('note/', views.note, name='note'),
    path('notesingle/', views.notesingle, name='notesingle'),

    path('createnote/', views.createnote, name='createnote'),
  




]