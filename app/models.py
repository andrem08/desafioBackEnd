from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from .validators import validate_nome, validate_nome_social, validate_not_empty, validate_contato

#Foi criado dois modelos, do cadastro do profissional, e da consulta médica, com o profissiional
# requerindo diversos validadores no arquivo validators.py. nome_social é um campo opcional
class Profissional(models.Model):
    nome = models.CharField(max_length=100, validators=[validate_nome])
    nome_social = models.CharField(max_length=100, blank=True, null=True, validators=[validate_nome_social])
    profissao = models.CharField(max_length=100, validators=[validate_not_empty])
    endereco = models.CharField(max_length=255, validators=[validate_not_empty])
    contato = models.CharField(max_length=100, validators=[validate_contato])

class ConsultaMedica(models.Model):
    profissional = models.CharField(max_length=100)  # Store the ID as a CharField

    def get_profissional(self):
        try:
            return Profissional.objects.get(id=self.profissional)
        except ObjectDoesNotExist:
            return None
