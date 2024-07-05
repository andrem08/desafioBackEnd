from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProfissionalViewSet,
    ConsultaMedicaViewSet,
    # profissional_detail
)

# Criando duas rotas, a primeira pro cadastro e a segunda para a consulta médica
router = DefaultRouter()
router.register(r'profissionais', ProfissionalViewSet)
router.register(r'consultas_medicas', ConsultaMedicaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
