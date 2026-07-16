"""Phase 02: OOP
Day: 19th
Part: 06
Topics Learned Today:-
1. Composition
2. Enum - Basic"""

from enum import Enum

# ==================== INHERITANCE EXAMPLE ====================

class Animal:
    """Base class representing any animal."""
    
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
        self.alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):  # Dog IS-A Animal
    """Dog inherits from Animal and adds its own behavior."""
    
    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)   # Call parent constructor
        self.breed = breed
        self.is_loyal = True

    def bark(self):
        print(f"{self.name} says Woof Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball!")


# ==================== COMPOSITION EXAMPLE ====================

class Engine:
    """Engine component that can be used by any vehicle."""
    
    def __init__(self, horsepower=200):
        self.horsepower = horsepower
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"Engine ({self.horsepower} HP) started!")
        else:
            print("Engine is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print("Engine stopped.")
        else:
            print("Engine is already off.")


class Car:
    """Car uses Composition - it HAS-A Engine."""
    
    def __init__(self, make, model, horsepower=200):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)   # Composition happens here

    def start_car(self):
        print(f"Starting {self.make} {self.model}...")
        self.engine.start()

    def stop_car(self):
        print(f"Stopping {self.make} {self.model}...")
        self.engine.stop()

# ========================== ENUM ==========================
# In my Library Management System, I compared like, 
# if data_to_work_with == "book" --> There were fixed possible values, either "book" or "member". But now that I have learned about enums, that's differently a change I'm going to make in the next version.

class DataType(Enum):

    BOOK = "book"
    MEMBER = "member"

# Now I can do:-
def compare(data_type: DataType):

    if data_type == DataType.BOOK:

        print("You've chosen Book.\n")
    
    elif data_type == DataType.MEMBER:

        print("You've chosen Members.\n")
    
    else:

        print("Invalid Input!\n")

# ==================== DEMO ====================

if __name__ == "__main__":
    print("=== Inheritance Example ===")
    dog = Dog(name="Buddy", fur_color="Golden", breed="Golden Retriever")
    dog.eat()
    dog.bark()
    dog.fetch()
    print()

    print("=== Composition Example ===")
    my_car = Car(make="Toyota", model="Fortuner", horsepower=280)
    my_car.start_car()
    my_car.stop_car()

    compare("book") # invalid
    compare(DataType.BOOK) # valid

    compare("member") #invalid
    compare(DataType.MEMBER) #valid

    for datatype in DataType:
        print(datatype)
        print(datatype.name)
        print(datatype.value)
    
    print(DataType("book"))
    # print(DataType("BOOK")) # This will raise ValueError since the value "BOOK" doesn't exist in DataType

    print(DataType.BOOK == "book")
    print(DataType.BOOK.value == "book")