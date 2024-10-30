from django.shortcuts import render
from .models import Tienda
# Create your views here.
def listadoTienda (request):
    LaTienda=Tienda.objects.all()
    return render(request,"GestionarTienda.html",{"mitienda":LaTienda})