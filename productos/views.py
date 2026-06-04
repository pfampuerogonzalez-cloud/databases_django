from django.shortcuts import render
from .models import producto

# Create your views here.

#CONTEXTO DE DATOS
def listar_productos(request):
    productos = producto.objects.all()
                                        #CONTEXTO=DATA(SIEMPRE SERÁ UN DICCIONARIO)
    return render(request,"index.html",        {"productos": productos}                                    )
