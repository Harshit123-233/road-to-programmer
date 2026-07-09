"""Phase 02: OOP
Day: 16th
Part: 03
Topics Learned Today:-
1. Inheritance
2. Polymorphism"""

class Person: # Parent class (or Base Class)

    def __init__(self, fname, lname):

        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Students(Person): # Child Class (or Derived Class)

    def __init__(self, fname, lname, year):
        super().__init__(fname, lname) # super() makes the child class inherit all the methods and properties from it's parent
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

person1 = Students("Harshit", "Kumar Singh", 2031)
person2 = Students("Aditi", "Singh", 2031)

person1.welcome()
person2.welcome()

class AnimeCharacters:

    def __init__(self, name, anime):
        
        self.name = name
        self.anime = anime

    def signature_move(self):
        print("Kamehameha")

class Char1(AnimeCharacters):
    pass

class Char2(AnimeCharacters):
    def signature_move(self):
        print("Rasengan")

class Char3(AnimeCharacters):
    def signature_move(self):    
        print("Gomu Gomu No Pistol")

Goku = Char1("Goku", "DBZ")
Naruto = Char2("Naruto", "Naruto")
Luffy = Char3("Luffy", "One Piece")

for x in (Goku, Naruto, Luffy): # Inheritance Class Polymorphism
    print(x.name)
    print(x.anime)
    x.signature_move()
    print("\n")