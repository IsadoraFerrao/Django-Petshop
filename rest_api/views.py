from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from reserva.models import Reserva, Petshop
from rest_api.serializers import AgendamentoModelSerializer,PetshopModelSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.

class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
class PetshopModelViewSet(ReadOnlyModelViewSet):
    queryset = Petshop.objects.all()
    serializer_class = PetshopModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

@api_view(['GET', 'POST']) #essa api pode ser acessada pelos métodos get e post
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    return Response({'hello': 'world API'})

