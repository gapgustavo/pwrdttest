import requests

class StarWarsAPIService:
    BASE_URL = "https://swapi.dev/api"

    def get_all_pages(self, endpoint, filters=None):
        url = f"{self.BASE_URL}/{endpoint}/"
        all_results = []
        while url:
            response = requests.get(url, params=filters)
            data = response.json()
            all_results.extend(data['results'])
            url = data.get('next')  # Atualiza a URL para a próxima página, se existir
        return all_results

    def get_characters(self, filters=None):
        return self.get_all_pages("people", filters)

    def get_planets(self, filters=None):
        return self.get_all_pages("planets", filters)

    def get_starships(self, filters=None):
        return self.get_all_pages("starships", filters)

    def get_films(self, filters=None):
        return self.get_all_pages("films", filters)
