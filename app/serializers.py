from rest_framework import serializers
from .models import Profissional, ConsultaMedica
from datetime import date

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    detalhes_profissional = serializers.SerializerMethodField(method_name='get_personal_data')
    data = serializers.SerializerMethodField(method_name='get_date')

    class Meta:
        model = ConsultaMedica
        fields = '__all__'

    def get_personal_data(self, obj):
        profissional_instance = obj.get_profissional()
        if profissional_instance:
            return ProfissionalSerializer(profissional_instance).data
        return None

    def get_date(self, obj):
        return date.today()