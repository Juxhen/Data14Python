import requests
import json
from pprint import pprint

dict_body = {'postcodes': ["B7 4BB", "KT3 5RU", "SW11 5LP", "KT1 2HT"]}
json_body = json.dumps(dict_body)
headers = {'Content-Type': 'application/json'}

# address = "https://api.postcodes.io/postcodes/B7 4BB"
# req_response = requests.get(address)


address = "https://api.postcodes.io/postcodes/"
req_response = requests.post(address, headers=headers, data=json_body)
# pprint(req_response.json())

pprint(req_response.json()['result'][0])

#print the postcode, eastings, northings and NUTS code for each result

# #my way
# for i in range(4):
#     result = req_response.json()['result'][i]
#     print(f"Postcodes: {result['result']['postcode']} Eastings: {result['result']['eastings']} Northings: {result['result']['northings']} and Nuts: {result['result']['codes']['nuts']}")

#davids better way
for postcode in req_response.json()['result']:
    result = postcode['result']
    print(f"Postcode: {result['postcode']} Eastings {result['eastings']} Northings {result['northings']} Nuts Code {result['codes']['nuts']}")


# print(req_response.status_code)
# print(req_response.headers)
# pprint(type(req_response.content))
#pprint(req_response.json())
# pprint(type(req_response.json()))

# result = req_response.json()['result']
# print(f"Eastings: {result['eastings']}; Northings: {result['northings']}")
# print(f"The Nuts code is {result['codes']['nuts']}")


# HTTP Status Codes
# 404 - Page Not Found
# 200 - OK
