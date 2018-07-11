from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('avaliarfotos/', views.AvaliacaoFotosView.as_view(), name='avaliar-fotos'),
    path('aprovarfoto/<int:foto_id>', views.AprovarFotoView.as_view(), {'aprovacao': True}, name='aprovar-foto'),
    path('rejeitarfoto/<int:foto_id>', views.AprovarFotoView.as_view(), {'aprovacao': False}, name='desaprovar-foto'),
]
