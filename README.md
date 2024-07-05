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


Para verificar o codigo, veja os arquivos /app/models, /app/serializers, /app/tests, /app/urls, /app/validators, e /app/views, além de desafioBackEnd/settings
O código foi feito sem plágio pelo autor André Miyazawa, com referencia em alguns videos do youtube como:

https://youtu.be/17KdirMbmHY?si=LGaFdF5odjVV5woR
https://youtu.be/B65zbFro2pU?si=wRxF7PGu22aPEAeq
https://youtu.be/DiSoVShaOLI?si=_XNcpd6zP1-R_6v-
https://youtu.be/uzO2PW5jNMk?si=bZvRkqb4NScwRmxM
https://youtu.be/44qdTGbWY8c?si=qu52D_Z9gIE8vcyV
https://youtu.be/jE37ZVeAqiI?si=PlhDsL7YYyYTKhFX
https://youtu.be/cEXt8hDyKQw?si=0vKW-_RSrkDfd3R6
https://youtu.be/t-uAgI-AUxc?si=5UTWEmV6b5EDO65I
