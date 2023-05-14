from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.response import Response
from django.http.response import JsonResponse
from post.models import Data
from post.api.serializers import PostSerializer
import pandas as pd
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
import post.api.hecca as hc
import post.api.data_processing as dp


class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Data.objects.all()

# Creacion del endpoint que guarda el arreglo con el .csv proveniente del front
    def post(request):
        data = request.data['data']
        name = request.data['name']
        area = request.data['area']
        Data.objects.create(name=name, data=data, area=area)
        return JsonResponse({'message': 'Data created'}, 200)


print(Data.objects.last().data)


@require_http_methods(['GET'])
def create_df(request):
    path = 'media/'+str(Data.objects.last().data)
    print(path)
    df_base = pd.read_csv(path, header=0)
    data = hc.fecha_cruda(df_base)
    data_missing = {'Validez': data[0],
                    'Porcentaje': data[1],
                    'N_faltante': data[2],
                    'Asho_inicio': data[3],
                    'Asho_fin':data[4] }
    return JsonResponse(data_missing)


