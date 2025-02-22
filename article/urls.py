from django.contrib import admin
from django.urls import path

from . import views

app_name = 'article'


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create, name='create'),
    path('article/<int:id>/', views.article, name='detail'),
]
