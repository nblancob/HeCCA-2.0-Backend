from django.contrib import admin
from post.models import Data

# Register your models here.


@admin.register(Data)
#Registro del modelo creado para almacenar los datos de la cuenca base
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'area', 'data']
