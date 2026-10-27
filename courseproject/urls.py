"""courseproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin

from django.urls import path, include 

from polls import views

urlpatterns = [
    # path('admin/', admin.site.urls), # Optionnel : désactivé pour le moment
    path('', views.home_view, name='home'),
    path('i18n/', include('django.conf.urls.i18n')), 
    path('doctors/', views.doctors_list_view, name='doctors_list'),
]
