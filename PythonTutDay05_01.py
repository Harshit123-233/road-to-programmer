"""Day 05 of Learning Python
Today I learned:-
1. Dictionaries
i. Accessing Dictionary Items
ii. Changing, Adding and Removing Dictionary Items
iii. Looping through a Dictionary
iv. Copy Dictionary
v. Nested Dictionary
vi. Dictionary Methods"""

dict1 = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(dict1)

print(len(dict1)) #printing how many items the dictionary contains

# Accessing the Dict Items
x = dict1["model"]
print(x)

x1 = dict1.get("year")
print(x1)

x2 = dict1.keys()
print(x2)

x3 = dict1.values()
print(x3)

x4 = dict1.items()
print(x4)

## Checking if an item exists or not
if "model" in dict1:
    print("Yes, 'model' does exists in dict1.")

# Changing Dict Values
dict1["year"] = 2018
print(dict1)

dict1.update({"year": 2020})
print(dict1)

# Removing Items
## Using pop() method
dict1.pop("model")
print(dict1)

## Other methods are popitem() or clear() method. Or by using del keyword.

# Loop through a dictionary
for x5 in dict1:
    print(x5)

for x6 in dict1.values():
    print(x6)

for x, y in dict1.items():
    print(x,y)

# Copy Dictionaries
dict2 = dict1.copy()
print(dict2)

dict3 = dict(dict1)
print(dict3)

# Nested Dictionaries
copperfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobis",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

## Accessing a Nested Dictionary
print(copperfamily["child2"]["name"])

## Looping through a Dictionary
for x10, obj in copperfamily.items():
    print(x10)

    for y1 in obj:
        print(y1 + ":", obj[y1])
