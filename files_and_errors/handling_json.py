import json
from pprint import pprint
#
# with open("film.json", "r") as jsonfile:
#     Film = json.load(jsonfile)
#
# # print(Film) # json reads things as dictionaries
#
# # print(Film['name'])
# # (json.dumps converts json into a string)
#
# with open("film.json", "w") as jsonfile:
#     json.dump(Film, jsonfile)


# class JsonMovies:
# #
# #     def __init__(self, name, year, studio):
# #         self.name = name
# #         self.year = year
# #         self.studio = studio
# #
# #
# # with open("film.json", "r") as jsonfile:
# #     film_dict = json.load(jsonfile)
# #
# #     # def read_json(self):
# #     #     with open("film.json", "r") as jsonfile:
# #     #         film_dict = json.load(jsonfile)
# #     #         film = film_dict.values
# #     #         return json.dump(film, jsonfile)
# #
# #
# # # new_movie = JsonMovies("JuxhenMovie",2010,"JuxhenStudio")
# # # JsonMovies.read_json(new_movie)
# #
# # shrek = JsonMovies(film_dict['name'], film_dict['year'], film_dict['studio'])
# #
# # print(shrek.name,shrek.year,shrek.studio)

class Film:
    def __init__(self, json_file_name):
        with open("film.json", "r") as jsonfile:
            film_dict = json.load(jsonfile)
        self.name = film_dict['name']
        self.year = film_dict['year']
        self.studio = film_dict['studio']


juxhen = Film("film.json")

print(juxhen.name, juxhen.year, juxhen.studio)