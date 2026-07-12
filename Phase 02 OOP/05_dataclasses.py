"""Phase 02: OOP
Day: 18th
Part: 05
Topics Learned Today:-
1. Dataclasses"""

from dataclasses import dataclass

@dataclass
class Expense:

    # def __init__(self, date_and_time: str, category: str, amount: float, description: str):
        
    #     self.date_and_time = date_and_time
    #     self.category = category
    #     self.amount = amount
    #     self.description = description

    date_and_time: str
    category: str
    amount: float
    description: str

    # def __str__(self):
        
    #     return f"You spend {self.amount} on {self.category} on {self.date_and_time} and gave this as an excuse: {self.description}"

expense1 = Expense(
    "7/12/2026",
    "Food",
    1000,
    "I was hungry af!"
)

expense2 = Expense(
    "7/12/2026",
    "Food",
    1000,
    "I was hungry af!"
)

print(expense1) # creates a __repr__() method on it's own

print(expense1.category)

print(expense1 == expense2) # creates a __eq__() method on it's own

expense1.amount = 500

print(expense1)