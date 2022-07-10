from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from AppStereo.models import Instrumentos, Musicos
from AppStereo.forms import MusicosForm, InstrumentosForm, UserRegisterForm
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

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
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            musico = Musicos (nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], instrumento=informacion['instrumento'], banda=informacion['banda'])
            musico.save()
            musicos = Musicos.objects.all()
            return render(request, "AppStereo/leerMusicos.html", {'musicos': musicos}) #redireccionamos al usuario a la pagina 'musicos'
    else:
        miFormulario = MusicosForm() #formulario vacio para construir el html
        return render(request, 'AppStereo/musicosForm.html', {'miFormulario': miFormulario})            


def instrumentosForm(request):
    if request.method == 'POST':
        miFormulario = InstrumentosForm(request.POST)
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            instrumento = Instrumentos(nombre=informacion['nombre'], modelo=informacion['modelo'], descripcion=informacion['descripcion'])
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



class MusicosList(LoginRequiredMixin, ListView):

    model = Musicos
    template_name = "AppStereo/musico_list.html"


class InstrumentosList(LoginRequiredMixin, ListView):

    model = Instrumentos
    template_name = "AppStereo/instrumento_list.html"


class MusicosDetail(LoginRequiredMixin, DetailView):

    model = Musicos
    template_name = "AppStereo/musico_detalle.html"


class InstrumentosDetail(LoginRequiredMixin, DetailView):

    model = Instrumentos
    template_name = "AppStereo/instrumento_detalle.html"


class MusicoCreacion(LoginRequiredMixin, CreateView):

    model = Musicos
    template_name = "AppStereo/musico_form.html"
    success_url = reverse_lazy('AppStereo:musicos')
    fields = ['nombre', 'apellido', 'edad', 'instrumento', 'banda']


class InstrumentoCreacion(LoginRequiredMixin, CreateView):

    model = Instrumentos
    template_name = "AppStereo/instrumento_form.html"
    success_url = reverse_lazy('AppStereo:instrumentos')
    fields = ['nombre', 'modelo', 'descripcion']


class MusicoUpdate(LoginRequiredMixin, UpdateView):

    model = Musicos
    template_name = "AppStereo/musico_form.html"
    success_url = reverse_lazy('LeerMusicos')
    fields = ['nombre', 'apellido', 'edad', 'instrumento', 'banda']


class InstrumentoUpdate(LoginRequiredMixin, UpdateView):

    model = Instrumentos
    template_name = "AppStereo/instrumento_form.html"
    success_url = reverse_lazy('AppStereo:instrumentos')
    fields = ['nombre', 'modelo', 'descripcion']


class MusicoDelete(LoginRequiredMixin, DeleteView):

    model = Musicos
    template_name = "AppStereo/musico_delete.html"
    success_url = reverse_lazy('AppStereo:musicos')


class InstrumentoDelete(LoginRequiredMixin, DeleteView):

    model = Instrumentos
    template_name = "AppStereo/instrumento_delete.html"
    success_url = reverse_lazy('AppStereo:instrumentos')                    

    
        
def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
      
            user = authenticate(username=usuario, password=clave)

            if user is not None:
                login(request, user)
                return render(request, 'AppStereo/inicio.html', {'mensaje':f'Bienvenido {usuario}'})
            else:
                return render(request, 'AppStereo/inicio.html', {'mensaje': 'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'AppStereo/inicio.html', {'mensaje': 'Usuario o contraseña incorrectos'})
    else:
        form = AuthenticationForm()
        return render(request, 'AppStereo/login.html', {'form': form})          


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'AppStereo/inicio.html', {'mensaje': f'Usuario {username} creado'})
        else:
            return render(request, 'AppStereo/inicio.html', {'mensaje': 'Error, no se pudo crear el usuario'})
    else:
        form = UserRegisterForm()
        return render(request, 'AppStereo/register.html', {'form': form})           
        

def logout_user(request):
    logout(request)
    return render(request, 'AppStereo/inicio.html')





           