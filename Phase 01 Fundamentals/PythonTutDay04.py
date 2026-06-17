"""Day 04 of Learning Python
Today I have learnt:-
1. List
i. Items are ordered, changeable and allow duplicates. List() constructor.
ii. Accessing List Items
iii. Changing and Inserting List Items
iv. Adding and Removing List Items
v. Looping Through List Items
vi. List Comprehension
vii. Sorting Lists
viii. Copying Lists
ix. Joining Lists

2. Tuples
i. Items are ordered, unchangeable and allow duplicates. tuple() constructor.
ii. Accessing Tuples
iii. Updating Tuples
iv. Unpacking a Tuple
v. Loop Tuples
vi. Join Tuples"""


List1 = ["apple", "banana", "banana", "cherry", "orange", "kiwi", "melon", "mango"] #Since it's indexed, duplicates are allowed

print(List1[0]) # Accessing List Items
print(List1[-2]) # Negative Indexing
print(List1[2:5]) # Accessing a Range

if "apple" in List1: # Checking if an item exists in the list
    print("Yes, 'apple' is in the fruits list.")

# Use of list() constructor
thisList = list(("India", "Russia", "Israel"))
print(thisList)

# Changing the items of a list
List1[4] = "guava"
print(List1)

## Changing a range
thisList[1:3] = ["Konoha", "Planet Vegeta"]
print(thisList)

## Adding items to a list
thisList.append("Foosha") #append
thisList.insert(3, "Karakura") #insert
thisList.extend(List1) #extend

## Removing items from the list
List1.remove("banana")
List1.pop(1)
del List1[0]
print(List1)

ListToClear = ['bat', 'ball', 'stumps', 'gloves']
ListToClear.clear()
print(ListToClear)

## Looping Through a List
thisList1 = ["python", "java", "c++"]
for x in thisList1: # Using a for loop
    print(x)

for i in range(len(thisList1)):
    print(thisList1[i])

i = 0
while i < len(thisList1): # Using a While Loop
    print(thisList1[i])
    i = i + 1

[print(x) for x in thisList1] # Using List Comprehension

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [x for x in fruits if "a" in x]
print(newList)

# Sorting Lists

## sort() method
ListToBeSorted = ["zebra", "tortoise", "yak", "owl", "parrot"]

ListToBeSorted.sort() #Sorts the list alphanumerically, ascending by default
print(ListToBeSorted)

ListToBeSorted.sort(reverse = True) #Sorts the list alphanumerically, descending
print(ListToBeSorted)

ListToBeSorted.sort(key = str.lower) #For Case Insensitive Sorting
print(ListToBeSorted)

ListToBeSorted.reverse() #Using the reverse() method
print(ListToBeSorted)

def myFunction(n): # Defining a custom function
    return abs(n - 50)

ListToBeSorted1 = [100, 50, 65, 82, 23]
ListToBeSorted1.sort(key = myFunction)
print(ListToBeSorted1)

# Copy Lists

ListToBeCopied1 = ["apple", "mango", "banana"]
ListToBeCopied2 = []

ListToBeCopied2 = ListToBeCopied1.copy() #Using the copy() Method
print(ListToBeCopied2)

## Other methods are list() or using the slice operator

# Joining Two Sets

ListToJoin1 = ["pushup", "pullup", "crunches"]
ListToJoin2 = ["squats", "situps", "hammer"]

listofExercises = ListToJoin1 + ListToJoin2 # Using the '+' operator
print(listofExercises)

##Other methods are :- appending each items one by one or by using the extend() method

Tuple1 = ("apple", "banana", "mango") # A tuple.
print(len(Tuple1))

#We access tuples just how we do with list.

#Tuples are unchangeable but we can workaround it by converting the tuple into a list. Doing the Change and then converting it back into a Tuple.

ListFromTuple = list(Tuple1)
ListFromTuple[1] = "kiwi"
Tuple1 = tuple(ListFromTuple)

print(Tuple1)

# Unpacking a Tuple:-
(green, brown, yellow) = Tuple1

print(green)
print(brown)
print(yellow)

## Using Asterisk (*):-
fruitsTuple = ("apple", "banana", "mango", "kiwi", "cherry")

(var1, var2, *var3) = fruitsTuple
print(var1)
print(var2)
print(var3)

(var4, *var5, var6) = fruitsTuple
print(var4)
print(var5)
print(var6)

#We loop Tuples exactly how we do in Lists.

# Join Tuples:-
## Method 1: Using the + Operator
TupleToBeJoined1 = ("bat", "ball", "stumps")
SingleTuple = ("gloves",)
ReqAccessories = TupleToBeJoined1 + SingleTuple
print(ReqAccessories)

## Method 2: If you want to multiply the content of a tuple a given number of times, let's say 2 times:-
TupleToBeJoined2 = ("India", "Russia", "Israel")
myTuple = TupleToBeJoined2 * 2
print(myTuple)