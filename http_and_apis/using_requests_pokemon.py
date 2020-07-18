import requests
import json
from pprint import pprint

address = "https://pokeapi.co/api/v2/pokemon/pikachu"
req_response = requests.get(address)
url_for_abilities = req_response.json()['abilities']

list_of_abilities_names = []
list_of_abilities_urls = []

for ability in url_for_abilities:
    result = ability['ability']
    list_of_abilities_urls.append(result['url'])
    list_of_abilities_names.append(result['name'])
    #print(f"The abilities are {result['url']}")

for x in range(2):
    req_response_abilities = requests.get(list_of_abilities_urls[x])
    get_ability_in_abilities = req_response_abilities.json()
    pprint(get_ability_in_abilities)

#print("Pikachu has the following moves, which have the following effects")

list_of_effect = []
for x in range(2):
    effect_changes = list_of_abilities_urls[x]
    req_response_effects = requests.get(effect_changes)
    url_for_effects = req_response_effects.json()['effect_entries']
    for effects in url_for_effects:
        #result = effects['effect']
        result = effects['short_effect']
        list_of_effect.append(result)
        #pprint(list_of_effect)
#
# print("\n")
# pprint(f"Pikachu's first ability is: {list_of_abilities_names[0]}, and the effect {list_of_effect[1]}")
# print("\n")
# pprint(f"Pikachu's second ability is: {list_of_abilities_names[1]}, and the effect {list_of_effect[-1]}")


with open("pokemonapi.txt", "a") as pokeapi:
    pokeapi.writelines(f"Pikachu's first ability is: {list_of_abilities_names[0]}, and the effect {list_of_effect[1]}")
    pokeapi.writelines("\n")
    pokeapi.writelines(f"Pikachu's second ability is: {list_of_abilities_names[1]}, and the effect {list_of_effect[-1]}")

# url_for_abilities = self.req_response.json()['abilities']
# for ability in url_for_abilities:
#     result = ability['ability']
#     self.list_of_abilities_urls.append(result['url'])
#     self.list_of_abilities_names.append(result['name'])
#
# for x in range(len(self.list_of_abilities_names)):
# # for x in len(self.list_of_abilities_names):
#     req_response_abilities = requests.get(self.list_of_abilities_urls[x])
#     get_ability_in_abilities = req_response_abilities.json()
#     #pprint(get_ability_in_abilities)
#
# for x in range(len(self.list_of_abilities_names)):
#     effect_changes = self.list_of_abilities_urls[x]
#     req_response_effects = requests.get(effect_changes)
#     url_for_effects = req_response_effects.json()['effect_entries']
#     for effects in url_for_effects:
#         #result = effects['effect']
#         result = effects['short_effect']
#         self.list_of_effect.append(result)
#         #pprint(self.list_of_effect[1])