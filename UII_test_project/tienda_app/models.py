from django.db import models

# Create your models here.
class Tienda(models.Model):
    id_tienda=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    correo_electronico=models.CharField(max_length=50)
    horario=models.CharField(max_length=50)
    tipo_de_producto=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre