# Star Wars API
Uma API RESTful para acessar informações do universo Star Wars, incluindo personagens, planetas, naves estelares e filmes. Esta API permite criar contas de usuário, autenticar-se e acessar dados detalhados com filtros personalizáveis.

## Sumário
- [Introdução](#introdução)
- [Estrutura](#estrutura-do-projeto)
- [Configuração](#configuração-do-ambiente-aws-lambda)
- [Endpoints](#endpoints)
  - [Autenticação](#autenticação)
  - [Recursos](#recursos)
  - [Estatísticas](#estatísticas)
- [Exemplos de Uso](#exemplos-de-uso)
- [Autoria](#autoria)

## Introdução
Esta API foi criada para fornecer informações detalhadas do universo Star Wars. Com endpoints separados para personagens, planetas, naves e filmes, é possível obter dados específicos e filtrar resultados conforme os requisitos solicitados.

## Estrutura do Projeto
- `lambda_function.py`: Função principal para roteamento de endpoints e autenticação.
- `data_handlers.py`: Manipuladores de dados para criação de conta, login, e consultas específicas.
- `swapi_client.py`: Classe para interface com a API SWAPI.
- `auth_service.py`: Serviço de autenticação e validação de API keys.
- `firebase_db.py`: Conexão e gerenciamento de dados no Firebase Database.

## Configuração do Ambiente AWS Lambda
Para configurar o ambiente do AWS Lambda com todos os pacotes necessários, siga as instruções abaixo:

1. Abra o CMD (Prompt de Comando).
2. Navegue até o diretório onde você deseja instalar os pacotes:

```bash
cd CAMINHO_PARA_PASTA_ONDE_ESTAO_OS_ARQUIVOS_DO_REPOSITORIO
```

3. Execute o seguinte comando para instalar os pacotes necessários no diretório `package`:

```bash
pip install --target=package --implementation cp --python-version 3.11 --only-binary=:all: --upgrade firebase-admin requests
```

4. Após a instalação, compacte a pasta `package`(com os arquivos do repositório dentro) em um arquivo ZIP para fazer o upload na AWS Lambda.

## Requisitos
- Python 3.11
- Bibliotecas requests e firebase-admin

## Endpoints
Abaixo estão os principais endpoints disponíveis na API.

### Autenticação
**Criar Conta**  
**Endpoint:** /create  
**Método:** POST  
**Descrição:** Cria uma nova conta de usuário.  
**Parâmetros:**
- username (string): Nome do usuário.
- password (string): Senha do usuário.

**Login**  
**Endpoint:** /login  
**Método:** POST  
**Descrição:** Realiza login do usuário e gera um token de acesso.  
**Parâmetros:**
- username (string): Nome do usuário.
- password (string): Senha do usuário.

### Recursos
**Listar Personagens**  
**Endpoint:** /characters  
**Método:** GET  
**Descrição:** Retorna uma lista de personagens.

**Listar Planetas**  
**Endpoint:** /planets  
**Método:** GET  
**Descrição:** Retorna uma lista de planetas.

**Listar Naves Estelares**  
**Endpoint:** /starships  
**Método:** GET  
**Descrição:** Retorna uma lista de naves estelares.

**Listar Filmes**  
**Endpoint:** /films  
**Método:** GET  
**Descrição:** Retorna uma lista de filmes.

### Estatísticas
**Estatísticas de Personagens**  
**Endpoint:** /statistics/characters  
**Método:** GET  
**Descrição:** Retorna estatísticas dos personagens.

**Estatísticas de Naves**  
**Endpoint:** /statistics/starships  
**Método:** GET  
**Descrição:** Retorna estatísticas das naves.

**Estatísticas de Planetas**  
**Endpoint:** /statistics/planets  
**Método:** GET  
**Descrição:** Retorna estatísticas dos planetas.

### Detalhes Específicos
**Detalhar Personagem**  
**Endpoint:** /characters/{character_name}  
**Método:** GET  
**Descrição:** Retorna detalhes específicos de um personagem pelo nome.

**Detalhar Nave**  
**Endpoint:** /starships/{starship_name}  
**Método:** GET  
**Descrição:** Retorna detalhes específicos de uma nave pelo nome.

**Detalhar Planeta**  
**Endpoint:** /planets/{planet_name}  
**Método:** GET  
**Descrição:** Retorna detalhes específicos de um planeta pelo nome.

## Exemplos de Uso
O código abaixo demonstra como utilizar cada um dos endpoints mencionados acima.

```python
import requests
import json

BASE_URL = 'URL_DE_SUA_AWS_LAMBDA'

def create_account(username, password):
    url = f'{BASE_URL}/create'
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    print('Create Account Response:', response.json())

def login(username, password):
    url = f'{BASE_URL}/login'
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    print('Login Response:', response.json())

def get_characters_list(headers):
    url = f'{BASE_URL}/characters'
    response = requests.get(url, headers=headers)
    print('Characters Response:', response.json())

def get_planets_list(headers):
    url = f'{BASE_URL}/planets'
    response = requests.get(url, headers=headers)
    print('Planets Response:', response.json())

def get_starships_list(headers):
    url = f'{BASE_URL}/starships'
    response = requests.get(url, headers=headers)
    print('Starships Response:', response.json())

def get_films_list(headers):
    url = f'{BASE_URL}/films'
    response = requests.get(url, headers=headers)
    print('Films Response:', response.json())

def get_stats_characters(headers):
    url = f'{BASE_URL}/statistics/characters'
    response = requests.get(url, headers=headers)
    print('Characters Statistics Response:', response.json())

def get_stats_starships(headers):
    url = f'{BASE_URL}/statistics/starships'
    response = requests.get(url, headers=headers)
    print('Starships Statistics Response:', response.json())

def get_stats_planets(headers):
    url = f'{BASE_URL}/statistics/planets'
    response = requests.get(url, headers=headers)
    print('Planets Statistics Response:', response.json())

def get_character(headers):
    url = f'{BASE_URL}/characters/Luke_Skywalker'
    response = requests.get(url, headers=headers)
    print('One Character Response:', response.json())

def get_starship(headers):
    url = f'{BASE_URL}/starships/x-wing'
    response = requests.get(url, headers=headers)
    print('One Starship Response:', response.json())

def get_planet(headers):
    url = f'{BASE_URL}/planets/tatooine'
    response = requests.get(url, headers=headers)
    print('One Planet Response:', response.json())

def get_character_filter(headers):
    url = f'{BASE_URL}/characters'
    filters = {'eye_color': 'blue', 'gender': 'male'}
    response = requests.post(url, headers=headers, json={'filters': filters})
    print('Filter Character Response:', response.json())

def get_starship_filter(headers):
    url = f'{BASE_URL}/starships'
    filters = {'passengers': '600'}
    response = requests.post(url, headers=headers, json={'filters': filters})
    print('Filter Starship Response:', response.json())

def get_planet_filter(headers):
    url = f'{BASE_URL}/planets'
    filters = {'climate': 'arid'}
    response = requests.post(url, headers=headers, json={'filters': filters})
    print('Filter Planet Response:', response.json())

def main():
    headers = {'x-api-key': 'SUA_API_KEY'}
    username = 'test_user'
    password = 'test_password'
    create_account(username, password)
    login(username, password)
    get_characters_list(headers)
    get_planets_list(headers)
    get_starships_list(headers)
    get_films_list(headers)
    get_stats_characters(headers)
    get_stats_starships(headers)
    get_stats_planets(headers)
    get_character(headers)
    get_starship(headers)
    get_planet(headers)
    get_character_filter(headers)
    get_starship_filter(headers)
    get_planet_filter(headers)

if __name__ == '__main__':
    main()
```

## Filtros
Para filtros específicos nos endpoints /characters, /planets, e /starships, você pode passar filtros no corpo da solicitação POST conforme exemplificado acima.

> **Observação:** Certifique-se de substituir 'x-api-key' pelo seu valor de API Key.

## Autoria
Este repositório foi desenvolvido para fornecer um serviço de consulta de dados do universo Star Wars de forma prática e escalável.

Este README cobre a estrutura básica e avançada da API, com detalhes de cada endpoint e exemplos de uso em Python, para facilitar a integração.
