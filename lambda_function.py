import json
from auth_service import AuthService
from data_handlers import *
from swapi_client import StarWarsAPIService

def lambda_handler(event, context):
    """Função principal para roteamento e verificação de API Key."""
    service = StarWarsAPIService()
    auth_service = AuthService()
    path = event.get('path')
    query_params = event.get('queryStringParameters', {})
    api_key = event.get('headers', {}).get('x-api-key')

    # Verifica a API key, exceto para os endpoints de criação e login
    if path not in ['/create', '/login'] and not auth_service.is_valid_api_key(api_key):
        return {
            'statusCode': 403,
            'body': json.dumps({'message': 'Invalid or missing API key'})
        }

    # Roteamento de endpoints
    if path == '/create':
        return create_account(event, auth_service)
    elif path == '/login':
        return login(event, auth_service)
    elif path.startswith('/characters/'):
        return get_character(path, auth_service)
    elif path.startswith('/planets/'):
        return get_planet(path, auth_service)
    elif path.startswith('/starships/'):
        return get_starship(path, auth_service)
    elif path == '/statistics/characters' and event.get('httpMethod') == 'GET':
        return get_statistics(auth_service.db.get_character_statistics())
    elif path == '/statistics/starships' and event.get('httpMethod') == 'GET':
        return get_statistics(auth_service.db.get_starships_statistics())
    elif path == '/statistics/planets' and event.get('httpMethod') == 'GET':
        return get_statistics(auth_service.db.get_planets_statistics())
    elif path == '/characters' and event.get('httpMethod') == 'POST':
        return filter_characters(event, auth_service)
    elif path == '/starships' and event.get('httpMethod') == 'POST':
        return filter_starships(event, auth_service)
    elif path == '/planets' and event.get('httpMethod') == 'POST':
        return filter_planets(event, auth_service)
    elif path in ['/characters', '/planets', '/starships', '/films']:
        return fetch_data(service, path, query_params, auth_service)

    # Retorna erro caso o endpoint não seja encontrado
    return {
        'statusCode': 404,
        'body': json.dumps({'message': 'Endpoint not found'})
    }
