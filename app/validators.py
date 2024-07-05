from django.core.exceptions import ValidationError
import re

def validate_nome(value):
    if len(value.split()) < 2:
        raise ValidationError("O nome deve consistir em pelo menos duas palavras.")

def validate_nome_social(value):
    if value and not value.strip():
        raise ValidationError("O nome social não pode estar vazio ou apenas espaço em branco.")

def validate_not_empty(value):
    if not value or not value.strip():
        raise ValidationError("Este campo não pode estar vazio ou apenas com espaços em branco.")

def validate_contato(value):
    # Example pattern: simple check for a phone number or email
    phone_pattern = re.compile(r"^\+?1?\d{9,15}$")
    email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if not phone_pattern.match(value) and not email_pattern.match(value):
        raise ValidationError("Contato deve ser um número de telefone ou endereço de e-mail válido.")