from django.urls import path
from . import views

#3 Configurar URLs para las páginas del sitio
urlpatterns = [
    path('', views.galeria, name='galeria'),
    path('imagen/<str:pk>/', views.verImagen, name='imagen'),
    path('agregar/', views.agregarImagen, name='agregar')
]
