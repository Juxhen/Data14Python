from json import JSONDecodeError
import requests


class PokemonStuff:

    def __init__(self, pokemon_name):
        try:
            self.pokemon_name = pokemon_name
            self.address = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
            self.req_response = requests.get(self.address)
            self.all_info = self.req_response.json()
            self.list_of_abilities_names = []
            self.list_of_abilities_urls = []
            self.list_of_effect = []
            self.list_of_game_indices = []
            self.list_of_game_names = []
            self.list_of_base_stats = []
            self.list_of_base_stats_names = []
            self.list_of_pokemon_type = []
            self.get_pokemon_type()
            self.appened_pokemon_type()
            self.get_abilities_and_effects()
            self.appened_abilities_and_effects_to_txt_file()
            self.get_name_of_games_appeared_in()
            self.appened_name_of_games_appeared_in()
            self.get_base_stats()
            self.appened_base_stats()
        except JSONDecodeError:
            print("This pokemon doesn't exist")

    # Gets the effect of each ability assigned to each pokemon where the language of that effect is in English,
    # it appends to 2 lists, one with the ability and one with the corresponding abilities effect in English.
    # For each row in the dictionary effect_entries search language and name where it's equal to 'en' - line 46
    def get_abilities_and_effects(self):
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

    # Gets the number of games the selected pokemon has appeared in, along with a list of all the versions names.
    def get_name_of_games_appeared_in(self):
        for row in self.all_info['game_indices']:
            self.list_of_game_indices.append(row['game_index'])
        for game_name in self.all_info['game_indices']:
            self.list_of_game_names.append(game_name['version']['name'])

    # Gets the base stats of each pokemon and appends it to 1 list,
    # and then checks each row for the name of that base stat which appends to a second list.
    def get_base_stats(self):
        for row in self.all_info['stats']:
            self.list_of_base_stats.append(row['base_stat'])
        for row2 in self.all_info['stats']:
            self.list_of_base_stats_names.append(row2['stat']['name'])

    # Gets the name of the type of pokemon selected and appends to a list.
    def get_pokemon_type(self):
        for row in self.all_info['types']:
            self.list_of_pokemon_type.append(row['type']['name'])

    # Opens a new txt file with the name of the pokemon entered and prints,
    # a custom message for each pokemon's number of abilities ranging from 1 to 4.
    def appened_abilities_and_effects_to_txt_file(self):
        with open(f"pokemonapi_{self.pokemon_name}.txt", "a") as pokeapi:
            pokeapi.writelines("\n")
            pokeapi.writelines("\n")
            if len(self.list_of_abilities_names) == 1:
                pokeapi.writelines(f"{self.pokemon_name.capitalize()}'s only ability is: {self.list_of_abilities_names[0]}, and the effect {self.list_of_effect[0]}")
            elif len(self.list_of_abilities_names) == 2:
                pokeapi.writelines(f"{self.pokemon_name.capitalize()}'s first ability is: {self.list_of_abilities_names[0]}, and the Effect: {self.list_of_effect[0]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name.capitalize()}'s second ability is: {self.list_of_abilities_names[1]}, and the Effect: {self.list_of_effect[1]}")
                pokeapi.writelines("\n")
            elif len(self.list_of_abilities_names) == 3:
                pokeapi.writelines(f"{self.pokemon_name.capitalize()}'s first ability is: {self.list_of_abilities_names[0]}, and the Effect: {self.list_of_effect[0]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name.capitalize()}'s second ability is: {self.list_of_abilities_names[1]}, and the Effect: {self.list_of_effect[1]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name.capitalize()}'s third ability is: {self.list_of_abilities_names[2]}, and the Effect: {self.list_of_effect[2]}")
                pokeapi.writelines("\n")
            elif len(self.list_of_abilities_names) == 4:
                pokeapi.writelines(f"{self.pokemon_name.capitalize()}'s first ability is: {self.list_of_abilities_names[0]}, and the Effect: {self.list_of_effect[0]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name.capitalize()}'s second ability is: {self.list_of_abilities_names[1]}, and the Effect: {self.list_of_effect[1]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name.capitalize()}'s third ability is: {self.list_of_abilities_names[2]}, and the Effect: {self.list_of_effect[2]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name.capitalize()}'s fourth ability is: {self.list_of_abilities_names[3]}, and the Effect: {self.list_of_effect[3]}")
                pokeapi.writelines("\n")

    # Appends to the text file created and adds the number of games and what games the pokemon has appeared in.
    def appened_name_of_games_appeared_in(self):
        with open(f"pokemonapi_{self.pokemon_name}.txt", "a") as pokeapi:
            pokeapi.writelines("\n")
            pokeapi.writelines("\n")
            pokeapi.writelines(f"{self.pokemon_name.capitalize()} has appeared in {len(self.list_of_game_indices)} Pokemon games\n")
            pokeapi.writelines(f"The games appeared in are: {self.list_of_game_names}")

    # Appends to the text file created and adds the pokemons base stats.
    def appened_base_stats(self):
        with open(f"pokemonapi_{self.pokemon_name}.txt", "a") as pokeapi:
            pokeapi.writelines("\n")
            pokeapi.writelines("\n")
            for x in range(len(self.list_of_base_stats_names)):
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.list_of_base_stats_names [x]} : {self.list_of_base_stats [x]}")

    # Creates the pokemon text file as it's the first method called in the __init__,
    # it also displays the pokemon name and type.
    def appened_pokemon_type(self):
        with open(f"pokemonapi_{self.pokemon_name}.txt", "a") as pokeapi:
            pokeapi.writelines(f"------------------------------{self.pokemon_name.upper()}------------------------------")
            pokeapi.writelines("\n")
            pokeapi.writelines("\n")
            pokeapi.writelines(f"{self.pokemon_name.capitalize()} is an {self.list_of_pokemon_type} type Pokemon")

# return a string with new lines, that iterates through number of games and appened as a str

