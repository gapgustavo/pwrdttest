import json

def create_account(event, auth_service):
    """Cria uma nova conta de usuário."""
    body = json.loads(event.get('body', '{}'))
    username = body.get('username')
    password = body.get('password')
    success, api_key = auth_service.create_account(username, password)
    if success:
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'User created', 'api_key': api_key})
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'User already exists'})
        }

def login(event, auth_service):
    """Realiza o login do usuário e retorna a API key."""
    body = json.loads(event.get('body', '{}'))
    username = body.get('username')
    password = body.get('password')
    api_key = auth_service.login(username, password)
    if api_key:
        return {
            'statusCode': 200,
            'body': json.dumps({'api_key': api_key})
        }
    else:
        return {
            'statusCode': 401,
            'body': json.dumps({'message': 'Invalid credentials'})
        }

def get_character(path, auth_service):
    character_name = path.split('/')[-1].replace('_', ' ').lower()
    cached_data = auth_service.db.get_character(character_name)

    if cached_data:
        return {
            'statusCode': 200,
            'body': json.dumps(cached_data)
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Character not found in the database'})
        }

def get_planet(path, auth_service):
    planet_name = path.split('/')[-1].replace('_', ' ').lower()
    cached_data = auth_service.db.get_planet(planet_name)

    if cached_data:
        return {
            'statusCode': 200,
            'body': json.dumps(cached_data)
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Planet not found in the database'})
        }

def get_starship(path, auth_service):
    starship_name = path.split('/')[-1].replace('_', ' ').lower()
    cached_data = auth_service.db.get_starship(starship_name)

    if cached_data:
        return {
            'statusCode': 200,
            'body': json.dumps(cached_data)
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Starship not found in the database'})
        }

def filter_characters(event, auth_service):
    body = json.loads(event.get('body', '{}'))
    filters = body.get('filters', {})
    filtered_characters = auth_service.db.get_filtered_characters(filters)

    if filtered_characters:
        return {
            'statusCode': 200,
            'body': json.dumps(filtered_characters)
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'No characters found with the given filters'})
        }

def filter_starships(event, auth_service):
    body = json.loads(event.get('body', '{}'))
    filters = body.get('filters', {})
    filtered_starships = auth_service.db.get_filtered_starships(filters)

    if filtered_starships:
        return {
            'statusCode': 200,
            'body': json.dumps(filtered_starships)
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'No starships found with the given filters'})
        }

def filter_planets(event, auth_service):
    body = json.loads(event.get('body', '{}'))
    filters = body.get('filters', {})
    filtered_planets = auth_service.db.get_filtered_planets(filters)

    if filtered_planets:
        return {
            'statusCode': 200,
            'body': json.dumps(filtered_planets)
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'No planets found with the given filters'})
        }

def get_statistics(statistics):
    return {
        'statusCode': 200,
        'body': json.dumps(statistics)
    }

def fetch_data(service, path, query_params, auth_service):
    """Busca dados da API ou do banco de dados, se disponíveis."""
    cached_data = auth_service.db.get_data_if_recent(path)
    
    if cached_data:
        return {
            'statusCode': 200,
            'body': json.dumps(cached_data)
        }
    else:
        if path == '/characters':
            response = service.get_characters(query_params)
        elif path == '/planets':
            response = service.get_planets(query_params)
        elif path == '/starships':
            response = service.get_starships(query_params)
        elif path == '/films':
            response = service.get_films(query_params)

        auth_service.db.save_data_with_timestamp(path, response)

        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
