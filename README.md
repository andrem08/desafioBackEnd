# Desafio Back end
## Descrição

Este projeto é uma aplicação web baseada em Django projetada para gerenciar perfis profissionais e consultas médicas. Inclui validação personalizada para campos de modelo para garantir a integridade dos dados.

## Bibliotecas usadas

- **Django**
- **Django REST Framework**

## Instalação

Para configurar este projeto localmente, siga estas etapas:

1. Clone o repositório:
   
    ```
    git clone https://github.com/yourusername/yourprojectname.git
    ```
 2. Instalar as dependências:

    (necessita do Python instalado)
    ```
    pip install django
    pip install djangorestframework
    pip install markdown       # Markdown support for the browsable API.
    pip install django-filter  # Filtering support
    ```
  3. Rode o django migrate:

    python manage.py migrate

  4. Para utilizar o programa, rode este comando:

    python manage.py runserver


Para editar e deletar tanto os registros dos profissionais quanto dos cadastros, basta pegar a url gerada pelo comando acima, selecionar a primeira opção (adicionar profissionais) ou a segunda (realizar uma consulta) e digitar o id do profissional ou da consulta respectiva. Por exemplo:

    http://127.0.0.1:8000/profissionais/1/

Neste caso poderá ver uma opção de DELETE para deletar o respectivo objeto, ou os campos abaixo para edita-los
