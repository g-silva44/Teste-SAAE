# Subir o container Docker
**Rodar:**\
```docker-compose up --build```

## Login do usuário root
```
Usuário: saae 
```

```
Senha: Saae1357
```

## Testes automatizados no container
**Rodar:**\
```docker-compose exec web python manage.py test ocorrencias```

## Desligar o container
**Rodar:**\
```docker-compose down```
\
# Rodar localmente
Navegar até a pasta raiz do projeto\
**No CMD**:\
```python manage.py runserver```\
**Acessar no navegador:** \
<ins>```http://127.0.0.1:8000```</ins>
