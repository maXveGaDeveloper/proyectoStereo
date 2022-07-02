from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from AppStereo.models import Instrumentos, Musicos
from AppStereo.forms import MusicosForm, InstrumentosForm
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.


def inicio(request):
    return render(request, 'AppStereo/inicio.html')

def musicos(request):
    return render(request, 'AppStereo/musicos.html')

def instrumentos(request):
    return render(request, 'AppStereo/instrumentos.html')

def albums(request):
    return render(request, 'AppStereo/albums.html')
    

def musicosForm(request):
    if request.method == 'POST':
        miFormulario = MusicosForm(request.POST) #aqui llega la info del html
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            musico = Musicos (nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], instrumento=informacion['instrumento'], banda=informacion['banda'])
            musico.save()
            return render(request, 'AppStereo/musicos.html') #redireccionamos al usuario a la pagina 'musicos'
    else:
        miFormulario = MusicosForm() #formulario vacio para construir el html
    return render(request, 'AppStereo/musicosForm.html', {'miFormulario': miFormulario})            


def instrumentosForm(request):
    if request.method == 'POST':
        miFormulario = InstrumentosForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            instrumento = Instrumentos (nombre=informacion['nombre'], modelo=informacion['modelo'], descripcion=informacion['descripcion'])
            instrumento.save()
            return render(request, 'AppStereo/instrumentos.html') #redireccionamos al usuario a la pagina 'instrumentos'
    else:
        miFormulario = InstrumentosForm() #formulario vacio para construir el html
    return render(request, 'AppStereo/instrumentosForm.html', {'miFormulario': miFormulario})       


def busquedaMusicos(request):
    try:
        if request.method == "GET":
            musico = request.GET["musicos"]
            musicos = Musicos.objects.filter(nombre__icontains=musico)
            if musicos:
                return render(
                    request,
                    "AppStereo/resultadosBusqueda.html",
                    {"musicos": musicos, "nombre": musico},
                )
            else:
                return HttpResponse(f"<h2>'{musico}' not found.</h2>")
    except MultiValueDictKeyError:
        return render(request, "AppStereo/busquedaMusicos.html")
        

def buscar(request):
    if request.GET["nombre"]:
        musico = request.GET["nombre"]
        musicos = Musicos.objects.filter(nombre__icontains=musico)
        return render(request, "AppStereo/resultadosBusqueda.html", {'musico': musicos, 'nombre': musico})

    else:

        respuesta = "No se ha ingresado ningun nombre"
    return HttpResponse(respuesta)    


def leerMusicos(request):
    musicos = Musicos.objects.all()
    return render(request, "AppStereo/leerMusicos.html", {'musicos': musicos})


def leerInstrumentos(request):
    instrumentos = Instrumentos.objects.all()
    contexto = {'instrumentos': instrumentos}
    return render(request, "AppStereo/leerInstrumentos.html", contexto)





      