
from django.contrib import admin
from django.urls import path
from .views import saludo, probandoTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludoMusicos/', saludo),
    path('probandoTemplate/', probandoTemplate),
]
