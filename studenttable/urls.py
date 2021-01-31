from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .import views

urlpatterns = [

    path('', views.table, name='table'),
    url(r'^edit/(?P<id>\d+)/$', views.edittable, {}, name='updatetable'),
    url(r'^delete/(?P<id>\d+)/$', views.deletetable, {}, name='updatetable'),
    path('createtable/', views.createtable, name='createtable'),
]
