from django.urls import path
from AppStereo import views


urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('musicos/', views.musicos, name='Musicos'),
    path('instrumentos/', views.instrumentos, name='Instrumentos'),
    path('albums/', views.albums, name='Albums'),
    path('musicosForm/', views.musicosForm, name='MusicosForm'),
    path('instrumentosForm/', views.instrumentosForm, name='InstrumentosForm'),
    path('busquedaMusicos/', views.busquedaMusicos, name='BusquedaMusicos'),
    path('buscar/', views.buscar, name='Buscar'),
]