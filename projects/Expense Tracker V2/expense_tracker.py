import json
from pathlib import Path
from datetime import datetime
import utils

class Expense:

    def __init__(self, date_and_time: str, category: str, amount: float, description: str):

        self.date_and_time = date_and_time
        self.category = category
        self.amount = amount
        self.description = description
    
    def expense_to_dict(self):

        expense_dict = dict(date_and_time = self.date_and_time, category = self.category, amount = self.amount, description = self.description)

        return expense_dict
    
class ExpenseTracker:

    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self):
        
        self.BASE_DIR = Path(__file__).resolve().parent
        self.db_path = self.BASE_DIR / "database" / "data.json"
        self.expense_list = [] # Will contain the expenses as Expense objects
    
    def dict_to_objects(self, db_list):

        """Used it to keep the code DRY. Currently used in load_data()"""

        sorted_expenses = sorted(
                db_list, 
                key=lambda x: datetime.strptime(x["date_and_time"], self.DATE_FORMAT)
                )

        self.expense_list.clear() # clears the list to avoid duplicating entries

        for index, expenses in enumerate(sorted_expenses, start = 1): # converts each dict to an Expense object

            entry = Expense(expenses.get("date_and_time"), expenses.get("category"), expenses.get("amount"), expenses.get("description"))

            self.expense_list.append(entry)

        return self.expense_list # returns a list containing all stored expenses as objects

    def load_data(self):

        """I need objects to work with and dictionaries inside list to store data"""

        try:

            if not self.db_path.exists():

                with open(self.db_path, "w", encoding = "utf-8") as file:

                    json.dump([], file)
                
                return []
            
            with open(self.db_path, "r", encoding = "utf-8") as file:


                data = json.load(file) #returns a list with expense entries inside as dictionaries

                return self.dict_to_objects(data)
        
        except FileNotFoundError:

            return []
        
        except json.JSONDecodeError:

            print("Database File Corrupted!\n")
            return []

        except PermissionError:

            print("Error: Permission denied when accessing 'data.json'.\n")
            return []

    def save_data(self, data_to_save) -> None:

        db_store_list = [] # This list will contain all the expenses as dictionaries

        for expenses in data_to_save:
            db_store_list.append(expenses.expense_to_dict()) # dictionaries -> Expenses Objects

        with open(self.db_path, "w", encoding = "utf-8") as file:
            json.dump(db_store_list, file, indent = 4)
    
    def add_expense(self):

        data_db = self.load_data()

        print("=" * 5,"Add Expense","=" * 5)

        DATE_OF_EXPENSE = utils.formatted_date_func()
        category = utils.get_valid_input(str, "Category: ")
        amount = utils.get_valid_input(float, "Amount: ")
        description = utils.get_valid_input(str, "Description: ")
        
        new_expense = Expense(DATE_OF_EXPENSE, category, amount, description)

        data_db.append(new_expense)

        self.save_data(data_db)

        print("Expense Successfully Added!\n")

    def view_expense(self):
        
        print("=" * 5,"Your Expenses","=" * 5)

        data_db = self.load_data()

        for index, expenses in enumerate(data_db, start = 1):
            print(f"{index}. Date & Time: {expenses.date_and_time}")
            print(f"\t Category: {expenses.category}")
            print(f"\t Amount: {expenses.amount:,.2f}")
            print(f"\t Description: {expenses.description}\n")
        
        print("=" * 30, "\n")

    def show_total(self):

        data_db = self.load_data()

        total_spend = []

        for index, expenses in enumerate(data_db, start = 1):

            total_spend.append(expenses.amount)
        
        print(f"Total Expend: {(sum(total_spend)):,.2f}\n")
    
    def show_by_category(self):

        data_db = self.load_data()

        category_totals = {}

        for expenses in data_db:

            category = expenses.category
            amount = expenses.amount

            category_totals[category] = category_totals.get(category, 0.0) + amount
        
        category_list = [{cat:amt} for cat, amt in category_totals.items()]

        print("=" * 5,"Showing Expenses by Category","=" * 5,"\n")

        for index, category_items in enumerate(category_list, start = 1):
            for key, value in category_items.items():
                print(f"{index}. {key}: {value}")
            
        print("\n")

    def delete_expense(self):

        print("=" * 5,"Your Current Expenses:-","=" * 5)
        self.view_expense()

        data_db = self.load_data()

        if not data_db:
            print("There are no expenses to delete!")
            return
        
        
        choice = utils.get_valid_input(int, "Enter the index of the expense you want to delete: ")

        index_to_delete = choice - 1 #adjusted for 0-based indexing (e.g., choice '1' is index 0)

        if 0 <= index_to_delete < len(data_db): 

            removed_item = data_db.pop(index_to_delete)
            self.save_data(data_db)
            print(f"Successfully deleted expense: {removed_item.category} - {removed_item.amount}\n")

        else:
            print("Error: Index number out of range!\n")

    def edit_expense(self):
        
        print("=" * 5,"Your Current Expenses:-","=" * 5)
        self.view_expense()

        data_db = self.load_data()

        if not data_db:
            print("There are no expenses to edit!")
            return
        
        choice = utils.get_valid_input(int, "Enter the index of the expense you want to edit: ")

        index_to_delete = choice - 1

        if 0 <= index_to_delete < len(data_db): 

            while True: # so that user can change multiple fields of an expense

                field_to_change = utils.get_valid_input(str, "What do you want to change (to end type n): ")

                if field_to_change.lower() == "category":

                    new_entry = utils.get_valid_input(str, f"Enter new {field_to_change}: ")

                    (data_db[index_to_delete]).category = new_entry

                    self.save_data(data_db)

                elif field_to_change.lower() == "description":

                    new_entry = utils.get_valid_input(str, f"Enter new {field_to_change}: ")

                    (data_db[index_to_delete]).description = new_entry

                    self.save_data(data_db)
                
                elif field_to_change.lower() == "amount":

                    new_entry = utils.get_valid_input(float, f"Enter new Amount: ")

                    (data_db[index_to_delete]).amount = new_entry

                    self.save_data(data_db)
                
                elif field_to_change.lower() == "n":

                    print("Returning back to main menu!")
                    break


                else:

                    print("Enter a valid field!")
                    continue

        else:
            print("Error: Index number out of range!\n")