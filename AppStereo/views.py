from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from AppStereo.models import Instrumentos, Musicos
from AppStereo.forms import MusicosForm, InstrumentosForm
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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



class MusicosList(ListView):

    model = Musicos
    template_name = "AppStereo/musico_list.html"


class InstrumentosList(ListView):

    model = Instrumentos
    template_name = "AppStereo/instrumento_list.html"


class MusicosDetail(DetailView):

    model = Musicos
    template_name = "AppStereo/musico_detalle.html"


class InstrumentosDetail(DetailView):

    model = Instrumentos
    template_name = "AppStereo/instrumento_detalle.html"


class MusicoCreacion(CreateView):

    model = Musicos
    template_name = "AppStereo/musico_form.html"
    success_url = reverse_lazy('AppStereo:musicos')
    fields = ['nombre', 'apellido', 'edad', 'instrumento', 'banda']


class InstrumentoCreacion(CreateView):

    model = Instrumentos
    template_name = "AppStereo/instrumento_form.html"
    success_url = reverse_lazy('AppStereo:instrumentos')
    fields = ['nombre', 'modelo', 'descripcion']


class MusicoUpdate(UpdateView):

    model = Musicos
    template_name = "AppStereo/musico_form.html"
    success_url = reverse_lazy('AppStereo:musicos')
    fields = ['nombre', 'apellido', 'edad', 'instrumento', 'banda']


class InstrumentoUpdate(UpdateView):

    model = Instrumentos
    template_name = "AppStereo/instrumento_form.html"
    success_url = reverse_lazy('AppStereo:instrumentos')
    fields = ['nombre', 'modelo', 'descripcion']


class MusicoDelete(DeleteView):

    model = Musicos
    template_name = "AppStereo/musico_delete.html"
    success_url = reverse_lazy('AppStereo:musicos')


class InstrumentoDelete(DeleteView):

    model = Instrumentos
    template_name = "AppStereo/instrumento_delete.html"
    success_url = reverse_lazy('AppStereo:instrumentos')                    

    
        

      