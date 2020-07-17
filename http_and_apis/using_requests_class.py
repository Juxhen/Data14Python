import requests
import json

class Postcodes:

    def __init__(self):
        self.dict_body = {'postcodes': ["B7 4BB", "KT3 5RU", "SW11 5LP", "KT1 2HT"]}
        self.dict_body = {}
        self.list_for_dict = []
        self.json_body = json.dumps(self.dict_body)
        self.address = "https://api.postcodes.io/postcodes/"
        self.headers = {'Content-Type': 'application/json'}
        self.req_response = requests.post(self.address, headers=self.headers, data=self.json_body)

    def add_postcodes(self):
        check = False
        while not check:
            user_input = input("would you like to add a postcode Y/N\n").upper
            if user_input == "Y":
                user_postcode_input = input("please enter a postcode")
                self.list_for_dict.append(user_postcode_input)
            else:
                check = True

