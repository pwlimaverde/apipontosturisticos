from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import EnderecoSerializer

class PontoTuristicoViewSet(ModelViewSet):

    queryset = Endereco.objects.all().order_by('-descricao')
    serializer_class = EnderecoSerializer
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    filterset_fields = ['id', 'linha1', 'linha2', 'cidade', 'estado', 'pais', 'latitude', 'longetude']
    filter_backends = [filters.SearchFilter]
    search_fields = ['linha1', 'linha2', 'cidade', 'estado', 'pais', 'latitude', 'longetude']
