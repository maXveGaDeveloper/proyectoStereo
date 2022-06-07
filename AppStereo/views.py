from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from AppStereo.models import Instrumentos, Musicos
from AppStereo.forms import MusicosForm, InstrumentosForm

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