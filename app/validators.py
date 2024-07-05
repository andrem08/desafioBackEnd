from django.core.exceptions import ValidationError
import re

def validate_nome(value):
    #Validando se o nome tem pelo menos 2 palavras (um nome e sobrenome)
    if len(value.split()) < 2:
        raise ValidationError("O nome deve consistir em pelo menos duas palavras.")

def validate_nome_social(value):
    #Validando se, caso preencham o nome social, ele nao esteja preenchido em vazio
    if value and not value.strip():
        raise ValidationError("O nome social não pode estar vazio ou apenas espaço em branco.")

def validate_not_empty(value):
    #Validando se o campo nao está vazio
    if not value or not value.strip():
        raise ValidationError("Este campo não pode estar vazio ou apenas com espaços em branco.")

def validate_contato(value):
    # Validando se corresponde a um telefone ou um email
    phone_pattern = re.compile(r"^\+?1?\d{9,15}$")
    email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if not phone_pattern.match(value) and not email_pattern.match(value):
        raise ValidationError("Contato deve ser um número de telefone ou endereço de e-mail válido.")
