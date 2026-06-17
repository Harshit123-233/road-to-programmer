"""Day 05 of Learning Python
Today I learned:-
1. Sets
i. Access Set Items
ii. Adding & Removing Set Items
iii. Looping through Sets
iv. Joining Sets
v. Frozenset and Frozenset Methods
vi. Set Methods"""

#Using the set() constructor
set1 = set(("apple", "banana", "mango"))
print(set1)

#Looping through the Set Items
for x in set1:
    print(x)

#Checking if the set contains a specified item or not
print("banana" in set1)
print("orange" not in set1)

#Adding Items in a Set
set1.add("orange")
print(set1)

##Using the update() method
set2 = {"kiwi", "guava", "pinapple"}
set1.update(set2)
print(set1)

#Removing Items from a Set
setToRemove = {"apple", "mango", "orange", "kiwi", "guava", "pinapple"}

##Using remove() method
setToRemove.remove("kiwi")
print(setToRemove)

##Using discard() method
setToRemove.discard("pineapple")
print(setToRemove)

##Then there are pop and clear methods and del keyword.

#Joining Two Sets

##Using union() method
set12 = {"cricket", "football", "hockey"}
set34 = {"tennis", "basketball", "volleyball"}

set1234 = set12.union(set34) # or set1 | set2
print(set1234)

##Using update() method
set12.update(set34)
print(set12)

##Using intersection() method
set56 = {"table", "chair", "sofa"}
set78 = {"stool", "kitchen shelf", "chair"}

set5678 = set56.intersection(set78) # or set1 & set2
print(set5678)

##Using difference() method
set91 = {"batter", "baller", "umpire"}
set19 = {"wicketkeeper", "fielder", "umpire"}

set9119 = set91.difference(set19) # or set91 - set19
print(set9119)

##Using symmetric_difference() method
set102 = {"CPU", "RAM", "ROM", "Motherboard"}
set201 = {"GPU", "PSU", "ROM", "RAM"}

set101102 = set102.symmetric_difference(set201) # or set102 ^ set201
print(set101102)

#Creating a frozenset using frozenset() constructor
frozenset1 = frozenset({"apple", "banana", "cherry"})
print(frozenset1)
print(type(frozenset1))