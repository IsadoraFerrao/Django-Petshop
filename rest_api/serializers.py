from rest_framework.serializers import ModelSerializer
from reserva.models import Reserva

class AgendamentoModelSerializer(ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'