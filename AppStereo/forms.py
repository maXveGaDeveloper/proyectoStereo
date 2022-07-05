from django import forms
from AppStereo.models import Musicos, Instrumentos, albums
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
