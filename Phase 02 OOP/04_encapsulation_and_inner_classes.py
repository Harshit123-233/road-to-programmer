"""Phase 02: OOP
Day: 17th
Part: 04
Topics Learned Today:-
1. Encapsulation
2. Inner Classes"""

class Person:

    def __init__(self, name, age, salary):
        
        self.name = name
        self.__age = age # Private Property
        self._salary = salary # Protected Property
        self.promotion_status = self.PromotionStatus()

    class PromotionStatus: # Inner Class

        def __init__(self):
            
            self.status = "Impossible"
        
        def possible(self):

            self.status = "Possible"
            print("There's a chance!")
        
        def impossible(self):

            self.status = "Not Anytime Soon"
            print("Not Anytime Soon")

    def promotion_status_employee(self):

        if self.promotion_status.status == "Possible":
            print("You're about to get a promotion!")
        else:
            print("Noob! Getting Nothing!")

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        
        else:
            print("Age must be positive!")
    
    def __gold_digger(self, salary): # Private Method
        if 10000000 <= salary <= 1000000000:
            return "Damn! You rich af!"
        
        else:
            return "Get a life!"
        
    def greet(self):

        message = self.__gold_digger(self._salary) # using the private method in a separate method

        print(f"You are {self.name} and you're {self.get_age()} years old. You earn {self._salary:,}. {message}")

person1 = Person("Harshit", 19, 150000000)
person1.greet()
# print(person1.__age) This will give an error since __age is a private property and cannot be accessed without a getter method.

print(f"Salary: {person1._salary:,.2f}") # can access it but shouldn't since _salary is a protected property

#Name Mangling
print(f"Age: {person1._Person__age}") #not recommended since it defeats the purpose of encapsulation

person1.promotion_status.possible()
person1.promotion_status_employee()