"""Phase 02: OOP
Day: 15th
Part: 02
Topics Learned Today:-
1. __init__() method
2. self Parameter
3. Class Properties
4. Class Methods"""

class Person:

    species = "Human" # Class Property

    def __init__(self, name, age):

        self.name = name # Instance Property
        self.age = age

    def __str__(self):
        
        return f"{self.name} ({self.age})"
    
    def celebrate_birthday(self):

        self.age += 1
        print(f"Happy Birthday! You are now {self.age} years old.")
    
    def greet(self):

        return "Hello, " + self.name
    
    def welcome(self):

        message = self.greet()
        print(f"{message}! Welcome to my Road To Programmer Journey!")

person1 = Person("Harshit", 19)

person1.welcome()
print(person1.__str__())

del Person.greet
del person1.age

# person1.welcome() This will now give an error!
# print(person1.__str__()) will give an error too!