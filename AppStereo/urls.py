from django.urls import path
from AppStereo import views
from AppStereo.views import MusicosList, InstrumentosList, MusicosDetail, InstrumentosDetail, MusicoCreacion,InstrumentoCreacion, MusicoUpdate, InstrumentoUpdate, MusicoDelete, InstrumentoDelete

urlpatterns = [
    
    path('', views.inicio, name='Inicio'),
    path('musicos/', views.musicos, name='Musicos'),
    path('instrumentos/', views.instrumentos, name='Instrumentos'),
    path('albums/', views.albums, name='Albums'),
    path('musicosForm/', views.musicosForm, name='MusicosForm'),
    path('instrumentosForm/', views.instrumentosForm, name='InstrumentosForm'),
    path('busquedaMusicos/', views.busquedaMusicos, name='BusquedaMusicos'),
    path('buscar/', views.buscar, name='Buscar'),
    path ('leerMusicos/', views.leerMusicos, name='LeerMusicos'),
    path ('leerInstrumentos/', views.leerInstrumentos, name='LeerInstrumentos'),
    path ('login', views.login_request, name='Login'),
    path ('register', views.register, name='Register'),
    
    path('musico/list/', MusicosList.as_view(), name='musico_list'),
    path('instrumento/list/', InstrumentosList.as_view(), name='instrumento_list'),
    path('musico/<pk>', MusicosDetail.as_view(), name='musico_detalle'),
    path('intrumento/<pk>', InstrumentosDetail.as_view(), name='instrumento_detalle'),
    path('musico/nuevo/', MusicoCreacion.as_view(), name='musico_nuevo'),
    path('instrumento/nuevo/', InstrumentoCreacion.as_view(), name='instrumento_nuevo'),
    path('musico/editar/<pk>', MusicoUpdate.as_view(), name='musico_editar'),
    path('instrumento/editar/<pk>', InstrumentoUpdate.as_view(), name='instrumento_editar'),
    path('musico/eliminar/<pk>', MusicoDelete.as_view(), name='musico_eliminar'),
    path('instrumento/eliminar/<pk>', InstrumentoDelete.as_view(), name='instrumento_eliminar'),


]