from expense_tracker import ExpenseTracker
import utils

def main():

    tracker = ExpenseTracker()

    while True:
        
        
        print("=" * 10, "Expense Tracker", "=" * 10, "\n")

        print("""Choose an option:
1. Add Expense
2. View Expenses
3. Show Total Expense
4. Show Spending by Category
5. Delete Expense
6. Edit Expense              
7. Exit
""")

        choice = utils.get_valid_input(int, "Enter Your Choice: ")

        if choice == 1:
            tracker.add_expense()
        elif choice == 2:
            tracker.view_expense()
        elif choice == 3:
            tracker.show_total()
        elif choice == 4:
            tracker.show_by_category()
        elif choice == 5:
            tracker.delete_expense()
        elif choice == 6:
            tracker.edit_expense()
        elif choice == 7:
            print("👋 Thanks for using Expense Tracker! Goodbye.")
            break
        else:
            print("Invalid option! Please choose 1-6.\n")


if __name__ == "__main__":

    print(utils.wish_me())

    main()