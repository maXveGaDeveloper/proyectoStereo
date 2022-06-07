from django.urls import path
from AppStereo import views


urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('musicos/', views.musicos, name='Musicos'),
    path('instrumentos/', views.instrumentos, name='Instrumentos'),
    path('albums/', views.albums, name='Albums'),
    
]