import requests
from Models.single_postcode_model import SinglePCModel
from config_manager import base_url


class SinglePC():

    def __init__(self, single_postcode):
        self.url = base_url() + single_postcode
        self.request = requests.get(self.url)
        self.header_details = self.request.headers
        self.response_json = self.request.json()

    def response(self):
        return SinglePCModel(self.response_json)


postcodes = ["KT3 5RU", "SW11 5LP", "TW5 9JF"]

pc_objects = []

for postcode in postcodes:
    pc_objects.append(SinglePC(postcode))

print(pc_objects)

for object in pc_objects:
    print(object.response().postcode, object.response().codes_nuts)