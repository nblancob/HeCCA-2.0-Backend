from rest_framework.serializers import ModelSerializer
from post.models import Data


class PostSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = ['name', 'area', 'data']
