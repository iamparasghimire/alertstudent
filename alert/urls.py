from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('password/', views.password, name='password'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),


]