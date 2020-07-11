#Extra practice using dictionaires
my_Dict = {"key": "value", "key2": 2}
my_Dict2 = {
    "key3": 10,
    "key4": 22,
    "name": "Juxhen",
    "funny": True
}
print(my_Dict)
print(my_Dict2)
print(type(my_Dict))

print(my_Dict2["key3"]) # dict[key] use square brackets in dictionaries

my_Dict["key"] = "new_value"
my_Dict["new_key"] = "no new value"
del my_Dict["new_key"] # remove keys

my_Dict.keys() # list all the keys
my_Dict.values() # list all the values

data14_dict = {
    "Trainees": ["Alex", "Anthony", "Ben"],
    "Trainers": ["David"]
}

dict1 = {
    "dict2": {
        "dict3": {
            "dict4": {
                "dict5": {
                    "Trainees": ["Juxhen", "Juxhen2", "Juxhen3"]
                }
            }
        }
    }
}

#print(data14_dict["Trainees"][0]) #double square brackets

print(dict1["dict2"]["dict3"]["dict4"]["dict5"]["Trainees"][2])
