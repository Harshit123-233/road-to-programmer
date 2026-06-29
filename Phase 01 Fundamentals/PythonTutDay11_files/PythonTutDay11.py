"""Today is Day 11 of my Python Learning Journey. Today, I have learnt:-
1. Python JSON:-
i. Parse JSON and Converting from Python to JSON
ii. Format and Order the Result"""

import json

# parse json
first_json = '{"name":"Sung Jinwoo", "age":24, "rank": "SSS"}'

first_dict = json.loads(first_json)

print(f"{first_dict["name"]} is {first_dict["age"]} years old and his rank is {first_dict["rank"]}.")

# converting from python to json
second_dict = {
    "name": "Cha Hae-in",
    "age": 23,
    "rank": "S"
}

second_json = json.dumps(second_dict)

print(second_json)
print(type(second_json))


my_info = { # these are not my real info, obviously 
  "name": "Harshit Kumar Singh",
  "age": 25,
  "married": True,
  "divorced": False,
  "spouse": "Aditi",
  "children": ("Goku","Vegeta"),
  "pets": "Mahoraga",
  "bad habits": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

my_info_json = json.dumps(my_info, indent = 4, sort_keys = True)

print(my_info_json)