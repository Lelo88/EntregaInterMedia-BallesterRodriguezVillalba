from django.urls import path

from .views import buscar_libros, busqueda_inicial, busqueda_libros, busqueda_sectores, busqueda_socios, form_inicial, form_libros, form_sectores, form_socios, inicio, libros

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('listado-libros/', libros, name='ListadoLibros'),
    path('formulario-libros/', form_libros, name='FormularioLibros'),
    path('formulario-sectores/', form_sectores, name='FormularioSectores'),
    path('formulario-socios/', form_socios, name='FormularioSocios'),
    path('formulario-inicial/', form_inicial, name='FormularioInicial'),
    path('busqueda-inicial/', busqueda_inicial, name='BusquedaInicial'),
    path('busqueda-libros/', busqueda_libros, name='BusquedaLibros'),
    path('busqueda-sectores/', busqueda_sectores, name='BusquedaSectores'),
    path('busqueda-socios/', busqueda_socios, name='BusquedaSocios'),
    path('buscar-libros/', buscar_libros, name='BuscarLibros'),
]