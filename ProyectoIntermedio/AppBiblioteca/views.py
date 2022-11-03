from django.shortcuts import render, redirect
from .models import Socio, Sector, Libro
from .forms import Libros, Socios, Sectores

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def libros(request):
    
    libro = Libro.objects.all()
    
    return render(request, 'listado_libros.html',{'lista_libros': libro})

def sectores(request):
    
    sector = Sector.objects.all()

    return render(request, 'listado_sectores.html', {'lista_sectores': sector})

def socios(request):
    
    socio = Socio.objects.all()
    
    return render(request, 'listado_socios.html', {'lista_socios': socio})

def form_libros(request):
    
    if request.method == "POST":
        libros = Libros(request.POST)
        
        if libros.is_valid():
            info_libros = libros.cleaned_data
            libro = Libro(titulo=info_libros['titulo'], sinopsis=info_libros['sinopsis'], autor=info_libros['autor'], codigo_libro=info_libros['codigo_libro'])
            libro.save()
            
            return redirect('ListadoLibros')
        
    else:
        libros = Libros()
    
    return render(request, 'formularioLibros.html', {'libros': libros})


def form_sectores(request):
    
    if request.method=='POST': 
        sectores = Sectores(request.POST)
        
        if sectores.is_valid():
            info_sectores = sectores.cleaned_data
            sector = Sector(color=info_sectores['color'], nombre=info_sectores['nombre'], cupo=info_sectores['cupo'], codigo_sector=info_sectores['codigo_sector'])
            sector. save()
            
            return redirect('ListadoSectores')

    else:
        sectores = Sectores()
        
    return render(request, 'formularioSectores.html',{'sectores': sectores})

def form_socios(request):
    
    if request.method == 'POST':
        socios = Socios(request.POST)
        
        if socios.is_valid():
            info_lectores = socios.cleaned_data
            lector = Socio(nombre=info_lectores['nombre'], apellido=info_lectores['apellido'], fecha_nac=info_lectores['fecha_nac'], codigo_socio=info_lectores['codigo_socio'])
            lector.save()
            
            return redirect('ListadoSocios')    
    
    else:
        socios = Socios()
        
    return render(request, 'formularioSocios.html', {'socios': socios})

def form_inicial(request):
    
    return render(request, 'formularioInicial.html')

def busqueda_inicial(request):
    
    return render(request, 'busquedaInicial.html')

def busqueda_libros(request):
    
    return render(request, 'busquedaLibros.html')

def buscar_libros(request):
    pass

def busqueda_sectores(request):
    
    return render(request, 'busquedaSectores.html')

def buscar_sectores(request):
    pass

def busqueda_socios(request):
    
    return render(request, 'busquedaSocios.html')

def buscar_socios(request):
    
    if request.GET['codigo_socio']:
        
        codigo_socio = request.GET['codigo_socio']
        socio = Socio.objects.get(codigo_socio=codigo_socio)
    
        return render(request, 'resultBusqLector.html', {'socio': socio,'codigo_socio': codigo_socio})
    else:
        respuesta = 'No enviaste datos'
        return render(request, 'resultBusqLector.html', {'respuesta': respuesta})