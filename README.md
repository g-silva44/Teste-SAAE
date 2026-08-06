# Apresentação
Projeto criado para teste de habilidade técnica do SAAE Juazeiro. Desenvolvido utilizando Python/Django, HTML, CSS e JavaScript  
Requisitos:
```
1. Tela de login.
2. Cadastro de bairros (CRUD).
3. Cadastro de ocorrências contendo: bairro, data/hora, descrição, status (Em
andamento/Resolvido) e responsável.
4. Listagem com pesquisa por bairro e status.
5. Dashboard inicial exibindo: Total de ocorrências Ocorrências em andamento
Ocorrências resolvidas  
6. Interface responsiva.
7. Validação de formulários.
8. Banco de dados SQLite.
```

# Documentação

# Como rodar

### Subir o container Docker
1. Abra o Docker Desktop
2. **Rodar:**  
```docker-compose up```
3. **Acesse no navegador:**
<ins>```http://localhost:8000/```</ins>

### Login do usuário root
```
Usuário: saae 
```

```
Senha: Saae1357
```

### Testes automatizados no container
**Rodar:**  
```docker-compose exec web python manage.py test ocorrencias```

### Desligar o container
**Rodar:**\
```docker-compose down```

### Rodar localmente
1. Navegar até a pasta raiz do projeto  
2. **No CMD**:  
```python manage.py runserver```  
3. **Acessar no navegador:**   
<ins>```http://127.0.0.1:8000```</ins>

## Testes automatizados localmente
**Rodar:**\
```python manage.py test ocorrencias```
