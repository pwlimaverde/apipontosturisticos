from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):

    queryset = PontoTuristico.objects.all().order_by('-descricao')
    serializer_class = PontoTuristicoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filterset_fields = ['id', 'nome', 'descricao', 'aprovado']
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'descricao', 'aprovado']
