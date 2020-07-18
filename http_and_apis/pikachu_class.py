import requests
import json
from pprint import pprint

class Pikachu:

    def __init__(self, pokemon_name):
        self.pokemon_name = pokemon_name
        self.address = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
        self.req_response = requests.get(self.address)
        self.all_info = self.req_response.json()
        self.list_of_abilities_names = []
        self.list_of_abilities_urls = []
        self.list_of_effect = []

    def abilities_and_effects(self):
        for row in self.all_info['abilities']:
            self.list_of_abilities_names.append(row['ability']['name'])
            self.list_of_abilities_urls.append(row['ability']['url'])
        for url in self.list_of_abilities_urls:
            get_effect = requests.get(url)
            effect_response = get_effect.json()['effect_entries']
            for row in effect_response:
                if row['language']['name'] == 'en':
                    append_with = row['short_effect']
                    self.list_of_effect.append(append_with)

    def appened_to_txt_file(self):
        with open("pokemonapi.txt", "a") as pokeapi:
            pokeapi.writelines(f"{self.pokemon_name} first ability is: {self.list_of_abilities_names[0]}, and the effect {self.list_of_effect[0]}")
            pokeapi.writelines("\n")
            pokeapi.writelines(f"{self.pokemon_name} second ability is: {self.list_of_abilities_names[1]}, and the effect {self.list_of_effect[1]}")
            pokeapi.writelines("\n")


play = Pikachu("machamp")
play.abilities_and_effects()
play.appened_to_txt_file()
