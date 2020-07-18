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
        self.list_of_game_indices = []
        self.list_of_game_names = []

    def abilities_and_effects(self):
        for row in self.all_info['abilities']:
            self.list_of_abilities_names.append(row['ability']['name'])
            self.list_of_abilities_urls.append(row['ability']['url'])
        for url in self.list_of_abilities_urls:
            get_effect = requests.get(url)
            effect = get_effect.json()['effect_entries']
            for row in effect:
                if row['language']['name'] == 'en':
                    short_effect = row['short_effect']
                    self.list_of_effect.append(short_effect)

    def name_of_games_appeared_in(self):
        for row in self.all_info['game_indices']:
            self.list_of_game_indices.append(row['game_index'])
        print(f"{self.pokemon_name} has appeared in {len(self.list_of_game_indices)} Pokemon games")
        for game_name in self.all_info['game_indices']:
            self.list_of_game_names.append(game_name['version']['name'])
        pprint(self.list_of_game_names)

    def appened_to_txt_file(self):
        with open("pokemonapi.txt", "a") as pokeapi:
            if len(self.list_of_abilities_names) == 1:
                pokeapi.writelines(f"{self.pokemon_name} only ability is: {self.list_of_abilities_names[0]}, and the effect {self.list_of_effect[0]}")
            elif len(self.list_of_abilities_names) == 2:
                pokeapi.writelines(f"{self.pokemon_name} first ability is: {self.list_of_abilities_names[0]}, and the effect {self.list_of_effect[0]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name} second ability is: {self.list_of_abilities_names[1]}, and the effect {self.list_of_effect[1]}")
                pokeapi.writelines("\n")
            elif len(self.list_of_abilities_names) == 3:
                pokeapi.writelines(f"{self.pokemon_name} first ability is: {self.list_of_abilities_names[0]}, and the effect {self.list_of_effect[0]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name} second ability is: {self.list_of_abilities_names[1]}, and the effect {self.list_of_effect[1]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name} third ability is: {self.list_of_abilities_names[2]}, and the effect {self.list_of_effect[2]}")
                pokeapi.writelines("\n")
            elif len(self.list_of_abilities_names) == 4:
                pokeapi.writelines(f"{self.pokemon_name} first ability is: {self.list_of_abilities_names[0]}, and the effect {self.list_of_effect[0]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name} second ability is: {self.list_of_abilities_names[1]}, and the effect {self.list_of_effect[1]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name} third ability is: {self.list_of_abilities_names[2]}, and the effect {self.list_of_effect[2]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name} fourth ability is: {self.list_of_abilities_names[3]}, and the effect {self.list_of_effect[3]}")
                pokeapi.writelines("\n")


play = Pikachu("pikachu")
# play.abilities_and_effects()
# play.appened_to_txt_file()
play.name_of_games_appeared_in()
