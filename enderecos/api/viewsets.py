from rest_framework.viewsets import ModelViewSet
from .serializers import EnderecoSerializer
from enderecos.models import Endereco


class EnderecosViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer