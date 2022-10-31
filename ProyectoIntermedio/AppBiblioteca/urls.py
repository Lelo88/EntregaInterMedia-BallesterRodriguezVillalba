from django.urls import path

from .views import form_libros, inicio, libros

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('listado-libros/', libros, name='ListadoLibros'),
    path('formulario-libros/', form_libros, name='FormularioLibros')
]