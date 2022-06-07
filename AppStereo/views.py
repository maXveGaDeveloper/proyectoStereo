from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def inicio(request):
    return render(request, 'AppStereo/inicio.html')

def musicos(request):
    return render(request, 'AppStereo/musicos.html')

def instrumentos(request):
    return render(request, 'AppStereo/instrumentos.html')

def albums(request):
    return render(request, 'AppStereo/albums.html')
    

