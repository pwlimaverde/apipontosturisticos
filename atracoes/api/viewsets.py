from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer

class PontoTuristicoViewSet(ModelViewSet):

    queryset = Atracao.objects.all().order_by('-descricao')
    serializer_class = AtracaoSerializer
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    filterset_fields = ['id', 'nome', 'descricao', 'horario_func', 'idade_minima']
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'descricao', 'horario_func', 'idade_minima']