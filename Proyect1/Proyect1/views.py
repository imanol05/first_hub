from ast import Return
from datetime import datetime
from fileinput import close
from multiprocessing import context
from pipes import Template
from xml.dom.minidom import Document
from django.http import HttpResponse
from datetime import datetime

def prueba(self):
    return HttpResponse("Hola Mundo")
def prueba_parametros(request):

    dia = datetime.now()
    parametro = f"El dia de hoy es: <br> {dia}"
    return HttpResponse(parametro)

def miNombre(request, nombre):
    usuario = f"Mi nombre es:<br><br> {nombre}"
    return HttpResponse(usuario)

def pruebaTemplate(request):
    miHtml = open( "H:\Python\CoderHouse\Tp3\Proyect1\Proyect1\plantillas\Template.html")

    plantilla = Template(miHtml.read())

    miHtml.close

    miContexto =context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)
