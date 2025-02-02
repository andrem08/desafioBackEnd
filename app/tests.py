from django.test import TestCase
from .models import Profissional, ConsultaMedica
from django.core.exceptions import ValidationError
import json

class ProfissionalConsultaMedicaTest(TestCase):

    # Criando tanto o cadastro do profissional quanto da consulta
    def setUp(self):
        self.profissional = Profissional.objects.create(
            nome="Nathan",
            nome_social="",
            profissao="Desenvolvedor",
            endereco="Rua 1",
            contato="123456789"
        )

        self.consulta = ConsultaMedica.objects.create(
            profissional=self.profissional.id
        )

    # Testando se os campos do cadastro estão corretos
    def test_profissional_fields(self):
        profissional = Profissional.objects.get(id="1")
        self.assertEqual(profissional.nome, "Nathan")
        self.assertEqual(profissional.nome_social, "")
        self.assertEqual(profissional.profissao, "Desenvolvedor")
        self.assertEqual(profissional.endereco, "Rua 1")
        self.assertEqual(profissional.contato, "123456789")

    # Testando se o profissional está correto
    def test_consulta(self):
        consulta = ConsultaMedica.objects.get(profissional=self.profissional.id)
        self.assertEqual(int(consulta.profissional), self.profissional.id)
