from django.urls import path
from tienda_app import views
urlpatterns = [
    path("",views.listadoTienda,name="listadoTienda")
]