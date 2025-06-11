from django.urls import path
from . import views
urlpatterns = [
    path('', views.buscar, name='home'),
    path('categoria/new/', views.crear_categoria, name='crear_categoria'),
    path('autor/new/', views.crear_autor, name='crear_autor'),
    path('post/new/', views.crear_post, name='crear_post'),
    path('buscar/', views.buscar, name='buscar'),
]
