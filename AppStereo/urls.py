from django.urls import path
from AppStereo import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('musicos/', views.musicos),
    path('instrumentos/', views.instrumentos),
    path('albums/', views.albums),
    
]