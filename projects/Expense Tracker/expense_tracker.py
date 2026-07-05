user_expense_record = {}
user_expense_category_record = {}
totalexpense = []

def viewfeatures():
    print(f"""Features:-
          1. Add Expense
          2. View Expense
          3. Show Total Expense
          4. Show Spending by Category
          5. Delete an Expense
          6. View Features
          7. Exit""")

def addExpense():
    dateofexpense = input("Enter the date of expense (YYYY/MM/DD): ")
    nthexpense = int(input("It's the nth expense of the day: "))
    amountspend = int(input("Enter the amount you spent: "))
    categoryspend = input("Enter where you spent it: ")
    description_Excuse = input("Do you want to say something about it?: ")
    if dateofexpense in user_expense_record:
        user_expense_record[dateofexpense][f'Spent {nthexpense}'] = {"Amount": amountspend, "Category": categoryspend, "Description": description_Excuse}
    else: 
        user_expense_record[dateofexpense] = {}
        user_expense_record[dateofexpense][f'Spent {nthexpense}'] = {"Amount": amountspend, "Category": categoryspend, "Description": description_Excuse}
    
    if categoryspend in user_expense_category_record:
        user_expense_category_record[categoryspend][f"Spend_{dateofexpense}_{nthexpense}"] = amountspend
    else:
        user_expense_category_record[categoryspend] = {f"Spend_{dateofexpense}_{nthexpense}": amountspend}
    
    totalexpense.append(amountspend)

def viewExpense():
    user_input1 = input("Do you want to see a specific expense [s] or the whole record [r] ?: ")
    if user_input1 == 's':
        user_input3 = input("Date(d) or Category(c) ?: ")
        if user_input3 == 'd':
            user_input4 = input("Enter the date you want to check the expense of (YYYY/MM/DD): ")
            if user_input4 not in user_expense_record:
                print(f"No expense made on {user_input4}.")
            else:
                print(user_expense_record[user_input4])
        else:
            print("Following are the categories in which you have spent so far:-")
            for x in user_expense_category_record:
                print(x)
            user_input5 = input("Enter the categories out of these: ")
            if user_input5 not in user_expense_category_record:
                print("The category you entered does not exist.")
            else:
                print(user_expense_category_record[user_input5])
    else:
        print("Okay Then, Here's The Complete Record!")
        print(user_expense_record)

def showtotalexpense():
    print(f"You have spent a total of {sum(totalexpense)} in Indian Rupees.")

def showspendbycategory():
    print("Alright. Here's your expenses by category:-")
    print(user_expense_category_record)

def deleting_record():
    print("Okay Then. So we are hiding the evidence now. Anyways.")
    user_input6 = input("Do you want to delete the whole record (a), delete a specific date (b), specific date's specific spend (c): ")
    if user_input6 == 'a':
        user_expense_record.clear()
        user_expense_category_record.clear()
        print("Done!")
    
    elif user_input6 == 'b':
        user_input7 = input("Enter the date which you want to delete (YYYY/MM/DD): ")
        if user_input7 not in user_expense_record:
            print("The entered date is not in the record!")
        else:
            expense_items = user_expense_record[user_input7]
            for spend_label, entry in expense_items.items():
                amount = entry["Amount"]
                category = entry["Category"]
                if amount in totalexpense:
                    totalexpense.remove(amount)
                category_key = f"Spend_{user_input7}_{spend_label.split()[1]}"
                if category in user_expense_category_record and category_key in user_expense_category_record[category]:
                    user_expense_category_record[category].pop(category_key)
                    if not user_expense_category_record[category]:
                        user_expense_category_record.pop(category)
            user_expense_record.pop(user_input7)
            print("Done!")
    
    elif user_input6 == 'c':
        user_input8 = input("Enter the date which you want to delete (YYYY/MM/DD): ")
        if user_input8 not in user_expense_record:
            print("The entered date is not in the record!")
        else:
            print(user_expense_record[user_input8])
            user_input9 = int(input("Which expense?: "))
            user_expense_record[user_input8].pop(f'Spent {user_input9}')
            print("Done!")

while True:
    viewfeatures()
    user_inp = int(input("What do you want to do: "))
    if user_inp == 1:
        addExpense()
    elif user_inp == 2:
        viewExpense()
    elif user_inp == 3:
        showtotalexpense()
    elif user_inp == 4:
        showspendbycategory()
    elif user_inp == 5:
        deleting_record()
    elif user_inp == 6:
        viewfeatures()
    elif user_inp == 7:
        exit()
    else:
        print("Enter a Valid Option!")