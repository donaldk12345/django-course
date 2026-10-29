"""courseproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include 

from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('about/', views.about_view, name='about'),
    path('doctors/', views.doctors_list_view, name='doctors_list'),
    path('doctor/<int:pk>/', views.doctor_detail_view, name='doctor_detail'),
    path('articles/', views.articles_list_view, name='articles_list'),
    path('article/<slug:slug>/', views.article_detail_view, name='article_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
