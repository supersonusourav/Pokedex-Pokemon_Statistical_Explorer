import requests

class PokeAPI:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/pokemon"

    def get_details(self, identifier):
        if not identifier: return None
        url = f"{self.base_url}/{str(identifier).lower().strip()}"
        try:
            r = requests.get(url, timeout=5)
            return r.json() if r.status_code == 200 else None
        except: return None

    def get_full_library(self, limit=1025):
        url = f"{self.base_url}?limit={limit}"
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                results = r.json()['results']
                library = []
                for index, p in enumerate(results):
                    p_id = index + 1
                    # We add a direct link to the sprite image for the table to use
                    sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{p_id}.png"
                    library.append({
                        "ID": p_id,
                        "Sprite": sprite_url, # New column for the image
                        "Name": p['name'].title(),
                        "Data Link": p['url']
                    })
                return library
            return []
        except: return []