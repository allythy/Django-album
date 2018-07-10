from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('meualbum/', views.EditarAlbumView.as_view()),
]
