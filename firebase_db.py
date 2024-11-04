import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime, timedelta

class FirebaseDB:
    def __init__(self):
        # Verifica se o Firebase já foi inicializado para evitar múltiplas inicializações
        if not firebase_admin._apps:
            cred = credentials.Certificate('CAMINHO_PARA_SUA_CREDENCIAL')  # Arquivo JSON com as credenciais do banco
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'URL_DA_SUA_DATABASE.'  # URL do seu banco
            })

    def create_user(self, username, password, api_key):
        ref = db.reference('users')
        if not ref.child(username).get():
            ref.child(username).set({'password': password, 'api_key': api_key})
            return True
        return False

    def login_user(self, username, password):
        ref = db.reference('users')
        user = ref.child(username).get()
        if user and user['password'] == password:
            return user['api_key']
        return None

    def validate_api_key(self, api_key):
        ref = db.reference('users')
        users = ref.get()
        for user_data in users.values():
            if user_data.get('api_key') == api_key:
                return True
        return False

    def save_data_with_timestamp(self, path, data):
        # Normaliza os dados antes de salvar
        normalized_data = []
        for item in data:
            normalized_item = item.copy()  # Cria uma cópia do item
            # Verifica se 'name' existe antes de normalizá-lo
            if 'name' in normalized_item:
                normalized_item['name'] = normalized_item['name'].lower()
            # Se o atributo for 'title', normaliza também, se necessário
            elif 'title' in normalized_item:
                normalized_item['title'] = normalized_item['title'].lower()

            normalized_data.append(normalized_item)

        ref = db.reference(path)
        ref.set({
            'data': normalized_data,
            'timestamp': datetime.utcnow().isoformat()
        })

    def get_data_if_recent(self, path):
        ref = db.reference(path)
        data = ref.get()
        if data:
            timestamp = data.get('timestamp')
            if timestamp:
                timestamp = datetime.fromisoformat(timestamp)
                # Verifica se os dados foram salvos nas últimas 24 horas
                if datetime.utcnow() - timestamp < timedelta(hours=24):
                    return data['data']
        return None
    
    def get_character(self, character_name):
        ref = db.reference('characters/data')
        characters = ref.get()

        if isinstance(characters, list):
            for character in characters:
                if isinstance(character, dict) and character.get('name') == character_name:
                    return character
        return None

    def get_character(self, character_name):
        ref = db.reference('characters/data')
        characters = ref.get()
        if isinstance(characters, list):
            for character in characters:
                if isinstance(character, dict) and character.get('name') == character_name:
                    return character
        return None

    def get_planet(self, planet_name):
        ref = db.reference('planets/data')
        planets = ref.get()
        if isinstance(planets, list):
            for planet in planets:
                if isinstance(planet, dict) and planet.get('name') == planet_name:
                    return planet
        return None

    def get_starship(self, starship_name):
        ref = db.reference('starships/data')
        starships = ref.get()
        if isinstance(starships, list):
            for starship in starships:
                if isinstance(starship, dict) and starship.get('name') == starship_name:
                    return starship
        return None

    def get_character_statistics(self):
        ref = db.reference('characters/data')
        characters = ref.get()
        statistics = {'eye_color': {}, 'hair_color': {}, 'skin_color': {}}
        
        if isinstance(characters, list):
            for character in characters:
                # Contagem para eye_color
                eye_color = character.get('eye_color')
                if eye_color:
                    statistics['eye_color'][eye_color] = statistics['eye_color'].get(eye_color, 0) + 1
                
                # Contagem para hair_color
                hair_color = character.get('hair_color')
                if hair_color:
                    statistics['hair_color'][hair_color] = statistics['hair_color'].get(hair_color, 0) + 1
                
                # Contagem para skin_color
                skin_color = character.get('skin_color')
                if skin_color:
                    statistics['skin_color'][skin_color] = statistics['skin_color'].get(skin_color, 0) + 1
        
        return statistics
    
    def get_starships_statistics(self):
        ref = db.reference('starships/data')
        starships = ref.get()
        statistics = {'manufacturer': {}, 'max_atmosphering_speed': {}, 'starship_class': {}}

        if starships:
            for starship in starships:
                # Contagem de 'manufacturer'
                manufacturer = starship.get('manufacturer')
                if manufacturer:
                    for m in manufacturer.split(', '):  # Divide múltiplos fabricantes
                        statistics['manufacturer'][m] = statistics['manufacturer'].get(m, 0) + 1
                
                # Contagem de 'max_atmosphering_speed'
                max_speed = starship.get('max_atmosphering_speed')
                if max_speed:
                    statistics['max_atmosphering_speed'][max_speed] = statistics['max_atmosphering_speed'].get(max_speed, 0) + 1

                # Contagem de 'starship_class'
                starship_class = starship.get('starship_class')
                if starship_class:
                    statistics['starship_class'][starship_class] = statistics['starship_class'].get(starship_class, 0) + 1

        return statistics


    def get_planets_statistics(self):
        ref = db.reference('planets/data')
        planets = ref.get()
        statistics = {'climate': {}, 'gravity': {}, 'terrain': {}}

        if planets:
            for planet in planets:
                # Contagem de 'climate'
                climate = planet.get('climate')
                if climate:
                    for cl in climate.split(', '):  # Divide múltiplos climas
                        statistics['climate'][cl] = statistics['climate'].get(cl, 0) + 1
                
                # Contagem de 'gravity'
                gravity = planet.get('gravity')
                if gravity:
                    statistics['gravity'][gravity] = statistics['gravity'].get(gravity, 0) + 1

                # Contagem de 'terrain'
                terrain = planet.get('terrain')
                if terrain:
                    for tr in terrain.split(', '):  # Divide múltiplos terrenos
                        statistics['terrain'][tr] = statistics['terrain'].get(tr, 0) + 1

        return statistics

    def get_filtered_characters(self, filters):
        ref = db.reference('characters/data')
        characters = ref.get()
        filtered_characters = []

        if isinstance(characters, list):
            for character in characters:
                match = True
                for key, value in filters.items():
                    if character.get(key) != value:
                        match = False
                        break
                if match:
                    filtered_characters.append(character)

        return filtered_characters

    def get_filtered_starships(self, filters):
        ref = db.reference('starships/data')
        starships = ref.get()
        filtered_starships = []

        if isinstance(starships, list):
            for character in starships:
                match = True
                for key, value in filters.items():
                    if character.get(key) != value:
                        match = False
                        break
                if match:
                    filtered_starships.append(character)

        return filtered_starships

    def get_filtered_planets(self, filters):
        ref = db.reference('planets/data')
        planets = ref.get()
        filtered_planets = []

        if isinstance(planets, list):
            for character in planets:
                match = True
                for key, value in filters.items():
                    if character.get(key) != value:
                        match = False
                        break
                if match:
                    filtered_planets.append(character)

        return filtered_planets
