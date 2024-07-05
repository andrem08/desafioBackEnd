from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from .models import Profissional, ConsultaMedica
from .serializers import ProfissionalSerializer, ConsultaMedicaSerializer
from .models import Profissional

class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer

class ConsultaMedicaViewSet(viewsets.ModelViewSet):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        profissional_id = self.request.query_params.get('profissional_id')
        if profissional_id is not None:
            queryset = queryset.filter(profissional_id=profissional_id)
        return queryset
