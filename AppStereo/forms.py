from django import forms
from AppStereo.models import Musicos, Instrumentos, albums

class MusicosForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    instrumento = forms.CharField(max_length=50)
    banda = forms.CharField(max_length=50)

class InstrumentosForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=50)

class albumsForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    artista = forms.CharField(max_length=50)
    fecha_lanzamiento = forms.DateField()
    genero = forms.CharField(max_length=50)        