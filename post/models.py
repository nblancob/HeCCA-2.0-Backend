from django.db import models

# Create your models here.

# Funcion para guardar el .csv
def upload_path(instance, filename):
    return '/'.join(['datas', str(instance.name), filename])

# Modelo de prueba que almacenara los datos de la cuenca base
class Data(models.Model):
    name = models.CharField(max_length=200, blank=False)
    area = models.IntegerField()
    data = models.FileField(blank=True, upload_to=upload_path)
