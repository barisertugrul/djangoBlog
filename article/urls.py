from django.contrib import admin
from django.urls import path

from . import views

app_name = 'article'


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('article/<int:id>/', views.detail, name='detail'),
    path('', views.articles, name='articles'),
    path('comment/<int:id>/', views.addComment, name='comment'),
]
