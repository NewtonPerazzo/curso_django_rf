from rest_framework.viewsets import ModelViewSet
from .serializers import AvaliacoesSerializer
from avaliacoes.models import Avaliacao


class AvaliacoesViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacoesSerializer