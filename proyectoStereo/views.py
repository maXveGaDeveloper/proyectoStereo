from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader


def saludo(request):
	return HttpResponse("Hola musicos!!!")


def probandoTemplate(self):
    #miHtml = open(r"C:\Users\Max\Desktop\django\proyectoFinal\proyectoStereo\proyectoStereo\plantillas\template.html")
    #miHtml.close()
    plantilla = loader.get_template('template.html')
    #miContexto = Context()
    documento = plantilla.render()
    return HttpResponse(documento)

