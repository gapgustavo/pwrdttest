import requests

BASE_URL = 'LAMBDA_URL'

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
    return response.json()

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
    username = 'test_user'
    password = 'test_password'
    create_account(username, password)
    login_request = login(username, password)
    headers = {'x-api-key': login_request['api_key']}
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
